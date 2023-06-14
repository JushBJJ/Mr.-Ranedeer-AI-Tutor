import backoff
import openai
import os
import tiktoken
import colorama


class GPT:
    def __init__(self, model, version, topic):
        self.model = model
        self.version = version
        self.topic = topic
        self.messages = [{"role": "system", "content": ""}]

    @backoff.on_exception(backoff.expo, openai.error.RateLimitError)
    def send(self):
        response = openai.ChatCompletion.create(model=self.model, messages=self.messages)

        content = response['choices'][0]['message']['content']
        return content, response["usage"]["total_tokens"]

    def setup_messages(self, content):
        self.messages = [{"role": "system", "content": content}]

    def append_message(self, role, content):
        self.messages.append({
            "role": role,
            "content": content
        })

    def save_response(self, response, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response)

    def print_title(self, title):
        print(colorama.Fore.YELLOW + title + colorama.Style.RESET_ALL)

    # Handle 'Plain Text' version separately
    def handle_plain_text(self, filenames, topics):
        plan_prompt = read_file(f"./v2.6/testing/prompts/{filenames[0]}")
        lesson_prompt = read_file(f"./v2.6/testing/prompts/{filenames[1]}")

        total_tokens = 0

        for topic in topics:
            self.print_title(f"-- Testing Plain Text on topic: {topic} --")
            self.setup_messages(plan_prompt)
            self.append_message("user", f"{topic}")
            plain_response, tokens = self.send()
            self.save_response(plain_response, f"./v2.6/testing/outputs/PlainText_{topic}_Planning.txt")

            total_tokens += tokens

            self.append_message("assistant", plain_response)
            self.append_message("assistant", lesson_prompt)
            self.append_message("user", "start lesson")
            plain_lesson_response, tokens = self.send()
            self.save_response(plain_lesson_response, f"./v2.6/testing/outputs/PlainText_{topic}_Lesson.txt")
            total_tokens += tokens
            print("Topic Finished. Total Tokens: ", total_tokens)

        print("Plain Text Finished Total Tokens: ", total_tokens)
        return total_tokens


def read_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        return f.read()


def print_with_color(text, color):
    print(color + text + colorama.Style.RESET_ALL)


def count_tokens(text):
    encoding = tiktoken.encoding_for_model("gpt-4")
    n = len(encoding.encode(text))
    print("Number of tokens: ", n)
    return n


if __name__ == "__main__":
    colorama.init()
    openai.api_key = os.environ["OPENAI_API_KEY"]
    MODEL = "gpt-4"

    topics = [
        "I want to learn The photoelectric effect",
        "I want to learn Integrals",
        "I want to learn Bernoulli Equation",
        "I want to learn Newton's Laws",
        "I want to learn English Grammar",
        "I want to learn Japanese",
        "I want to learn Machine Learning",
        "I want to learn Python"
    ]

    versions = {
        "Plain Text": ["Plain_Plan.txt", "Plain_lesson.txt"],
        "Mr. Ranedeer v2.5": ["Mr_Ranedeer_v2.5.json"],
        "Mr. Ranedeer v2.6": ["Mr_Ranedeer_v2.6.txt"]
    }

    total_tokens = 0

    for version, filenames in versions.items():

        tester = GPT(MODEL, version, topics)
        tester.print_title(f"=== Testing {version} ===")

        # If 'Plain Text', handle separately
        if version == "Plain Text":
            total_tokens += tester.handle_plain_text(filenames, topics)
        else:
            for filename in filenames:
                content = read_file(f"./v2.6/testing/prompts/{filename}")

                for topic in topics:

                    tester.setup_messages(content)

                    tester.print_title(f"-- Testing {version} on topic: {topic} --")
                    tester.append_message("user", f"/plan {topic}")
                    mr_ranedeer_plan_response, token = tester.send()
                    tester.save_response(mr_ranedeer_plan_response, f"./v2.6/testing/outputs/{version}_{topic}_planning.txt")
                    tester.append_message("system", mr_ranedeer_plan_response)

                    total_tokens += token

                    tester.append_message("user", "/start")
                    mr_ranedeer_lesson_response, token = tester.send()
                    tester.save_response(mr_ranedeer_lesson_response, f"./v2.6/testing/outputs/{version}_{topic}_lesson.txt")
                    total_tokens += token

                    print("Topic Finished. Total Tokens: ", total_tokens)

                print(f"{version} Finished Total Tokens: ", total_tokens)

    evaluator = GPT(MODEL, version, topics)
    # Evaluate
    with open("./v2.6/testing/prompts/evaluator.txt", "r") as f:
        evaluation = f.read()

    plain_output = ""
    mr_ranedeer_output = ""

    for topic in topics:
        plain_plan = read_file(f"./v2.6/testing/outputs/PlainText_{topic}_Planning.txt")
        plain_lesson = read_file(f"./v2.6/testing/outputs/PlainText_{topic}_Lesson.txt")
        mr_ranedeer_plan = read_file(f"./v2.6/testing/outputs/Mr. Ranedeer v2.6_{topic}_planning.txt")
        mr_ranedeer_lesson = read_file(f"./v2.6/testing/outputs/Mr. Ranedeer v2.6_{topic}_lesson.txt")

        plain_output = f"Topic: {topic}\nPlan:\n{plain_plan}\nLesson:\n{plain_lesson}\n\n"
        mr_ranedeer_output = f"Topic: {topic}\nPlan:\n{mr_ranedeer_plan}\nLesson:\n{mr_ranedeer_lesson}\n\n"

        evaluator_prompt = read_file("./v2.6/testing/prompts/evaluator.txt")

        evaluator_prompt = evaluator_prompt.replace("{{MR. RANEDEER OUTPUT HERE}}", mr_ranedeer_output)
        evaluator_prompt = evaluator_prompt.replace("{{PLAIN OUTPUT HERE}}", plain_output)

        evaluator.setup_messages(evaluator_prompt)
        evaluation_response, token = evaluator.send()

        # Save results to ./results/evaluation.txt
        with open(f"./v2.6/testing/results/PLAINTEXT_VS_MR_RANEDEER_{topic}_EVALUATION.txt", "w", encoding="utf-8") as f:
            f.write(f"== PLAIN TEXT vs MR. RANEDEER - TOPIC: {topic} ==\n")
            f.write(evaluation_response)

        print(evaluation_response)
        total_tokens += token
        print("Total Tokens Used Overall: ", total_tokens)

    # TODO v2.5 vs v2.6
    cost = 0.06 * (total_tokens / 1000)
    print("Evaluation Finished. Total Tokens: ", total_tokens)
    print(f"Total Cost to evaluate: Approx. ${cost}")

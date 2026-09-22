# SmartSpend: Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

The private-data scenario chosen for this project is personal expense management. The system contains a small set of private expense records consisting of Food, Travel, Books, Shopping, and Entertainment expenses. The monthly budget used in this project is Rs. 3,000.

The private expense data is:

| Category | Amount |
|---|---:|
| Food | Rs. 850 |
| Travel | Rs. 500 |
| Books | Rs. 700 |
| Shopping | Rs. 450 |
| Entertainment | Rs. 300 |

The total expense is Rs. 2,800, leaving Rs. 200 from the monthly budget.

This scenario was selected because the same private-data question can be handled differently by a plain chatbot, a rule-based workflow, and an AI agent. It also demonstrates the difference between an LLM response, predefined program rules, and an LLM that can use tools.

---

## 2. Plain Chatbot

The plain chatbot represents an approach where an LLM mainly provides responses based on the user's question. It does not use a tool to retrieve or calculate information from the private expense records. Therefore, it cannot reliably provide the exact amount spent on Books, the total expense, or the category with the highest spending.

In this project, the chatbot responds that it cannot access the user's private expense data. This shows an important limitation of using an LLM alone for private-data questions. The chatbot can understand the type of question and produce a natural-language response, but it does not have a data-access tool connected to the private expense records.

The main requirement of the plain chatbot is an LLM. It does not require a separate expense lookup tool, calculator tool, or decision loop. Its main limitation in this scenario is that it cannot use the private data to produce reliable numerical answers.

---

## 3. Rule-Based Workflow

The rule-based workflow uses predefined Python functions and conditions to process the private expense data. It does not use an LLM.

The workflow directly accesses the expense dictionary and applies fixed rules. One function calculates the total expense, another identifies the category with the highest expense, and another calculates the remaining budget.

For the selected data, the workflow calculates a total expense of Rs. 2,800, identifies Food as the highest expense category with Rs. 850, and calculates the remaining budget as Rs. 200.

The main advantage of this approach is predictable behaviour. Since the rules are explicitly written in Python, the same input produces the same result. However, its limitation is flexibility. If a user asks a new type of question that has not been covered by the predefined rules, the workflow needs additional programming logic.

---

## 4. AI Agent

The AI agent combines an LLM, tools, and a loop to handle questions about the private expense data.

The tools created for this project are an expense lookup tool, a calculation tool, and a remaining-budget tool. The expense lookup tool retrieves the amount for a particular category. The calculation tool performs arithmetic, and the remaining-budget tool calculates the unused part of the monthly budget.

The agent receives a question, determines which tool is appropriate, uses that tool, observes the returned result, and then produces a final answer. This demonstrates the basic agentic pattern of LLM + Tools + Loop.

For example, when asked about Books, the agent uses the expense lookup tool and obtains Rs. 700. When asked for the total expense, it uses the calculation tool and obtains Rs. 2,800. When asked about the remaining budget, it uses the budget tool and obtains Rs. 200.

The agent is more flexible than a fixed workflow because different questions can lead to different tool selections. However, an agent also requires more components and can be more complex to design, test, and control.

---

## 5. Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | High for natural-language responses, but cannot use the private expense data | Low to medium because behaviour is based on predefined rules | High because it can understand different questions and select tools |
| Decision-making | Mainly generates a response using the LLM | Follows fixed conditions and predefined program logic | Uses the LLM to decide which available tool is needed |
| Tool usage | No tools | Uses predefined Python functions/rules | Uses multiple tools selected according to the task |
| Private-data access | No direct access to the private expense records | Direct access through Python code | Accesses private data through tools |
| Multi-step task handling | Limited because there is no tool loop | Possible only when explicitly programmed | Can perform multiple tool calls and continue until the task is completed |
| Automation | Mainly response generation | High for fixed and repetitive calculations | High for flexible tasks involving tool selection and multiple steps |
| Reliability | Can give an unsupported response when private data is unavailable | High and predictable for predefined rules | Depends on correct tool selection and tool results |

---

## 6. Suitability Analysis

For the personal expense management scenario, the AI agent is suitable when the user wants to ask different types of questions about the private data and expects the system to select the appropriate operation. The agent can use different tools for expense lookup, calculations, and budget checking.

The rule-based workflow is also suitable when the required operations are fixed and predictable. For example, if the main requirements are always calculating total expenses, finding the highest category, and checking the remaining budget, predefined Python rules can perform these operations consistently.

The plain chatbot is suitable when the task mainly requires natural-language interaction and does not require access to private numerical data. In this scenario, however, it cannot provide reliable answers to questions that depend on the private expense records because it does not access that data.

Therefore, the choice depends on the requirements of the problem. Flexible tool selection and multi-step handling make the AI agent useful for varied expense questions, while predictable fixed calculations can be handled by a rule-based workflow.

---

## 7. Conclusion

A plain chatbot, a rule-based workflow, and an AI agent solve problems in different ways. A plain chatbot mainly uses an LLM to understand a request and generate a response, but it does not automatically have access to private data or external tools. A rule-based workflow follows predefined steps and conditions, making it useful for predictable and repetitive tasks where the required logic is already known.

An AI agent combines an LLM, tools, and a loop. It can understand the user's request, select an appropriate tool, use the tool, observe the result, and continue with further actions when required. This makes the agent suitable for tasks that require flexible decision-making, private-data access through tools, and multiple steps.

Overall, a chatbot is appropriate for general conversational responses, a rule-based workflow is appropriate for fixed and predictable processes, and an AI agent is appropriate for flexible tasks that require tool usage and multi-step task handling.
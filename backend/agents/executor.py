from backend.tools.registry import TOOLS


class Executor:

    def execute(self, plan: list, state: dict):

        results = []

        for step in plan:

            tool = TOOLS.get(step)

            if not tool:
                continue

            print(f"Executing: {step}")

            #pass state to every tool
            state = tool(state)

            results.append({
                "step": step,
                "state": state
            })

        return state, results
    

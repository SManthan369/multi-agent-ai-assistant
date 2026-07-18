import os


def human_approval(state):
    """
    Human approval node.

    Interactive locally.
    Automatically approves in CI/testing.
    """

    # Automatically approve in GitHub Actions or automated tests
    if os.getenv("CI") == "true" or os.getenv("PYTEST_CURRENT_TEST"):

        state["approval"] = state.get("approval", True)

        if state["approval"]:
            state["messages"].append("Plan Approved (Auto)")
        else:
            state["messages"].append("Plan Rejected (Auto)")

        return state

    print("\n" + "=" * 70)
    print("EXECUTION PLAN")
    print("=" * 70)
    print(state["plan"])

    while True:

        choice = input("\nApprove this plan? (y/n): ").strip().lower()

        if choice in ("y", "yes"):
            state["approval"] = True
            state["messages"].append("Plan Approved")
            break

        if choice in ("n", "no"):
            state["approval"] = False
            state["messages"].append("Plan Rejected")
            break

        print("Please enter y or n.")

    return state
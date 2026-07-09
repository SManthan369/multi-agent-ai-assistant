def human_approval(state):

    print("\n" + "=" * 70)
    print("EXECUTION PLAN")
    print("=" * 70)
    print(state["plan"])

    while True:

        choice = input("\nApprove this plan? (y/n): ").strip().lower()

        if choice in ["y", "yes"]:
            state["approval"] = True
            state["messages"].append("Plan Approved")
            break

        elif choice in ["n", "no"]:
            state["approval"] = False
            state["messages"].append("Plan Rejected")
            break

        else:
            print("Please enter y or n.")

    return state
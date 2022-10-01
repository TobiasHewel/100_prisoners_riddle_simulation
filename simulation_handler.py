import simulation


def run_instances(amount, boxes, tactic):
    results = []

    if boxes % 2 == 1:
        print(
            f"There has to be an evan number of boxes, you entered {boxes} which is an odd number.")
        return

    for index in range(amount):
        results.append(simulation.run_instance(boxes, tactic))

    total_result = {
        "passed": 0,
        "failed": 0
    }

    for result in results:
        all_people_passed = True

        for person in result:
            if person["found_id"] == False:
                all_people_passed = False

        if all_people_passed:
            total_result["passed"] += 1
        else:
            total_result["failed"] += 1

    print(total_result)

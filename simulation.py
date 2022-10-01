import random


def run_instance(numbers_of_boxes, tactic):
    results = []

    boxes = list(range(0, numbers_of_boxes))
    random.shuffle(boxes)

    for id in range(0, numbers_of_boxes):
        found_id = False

        match tactic:
            case "pick_at_random":
                box_picks = boxes
                random.shuffle(box_picks)

                for box_pick_id in range(0, numbers_of_boxes // 2):
                    if box_picks[box_pick_id] == id:
                        found_id = True
            case "follow_the_number_trail":
                next_box_pick_id = id

                for box_pick in range(0, numbers_of_boxes // 2):
                    if boxes[next_box_pick_id] == id:
                        found_id = True

                    next_box_pick_id = boxes[next_box_pick_id]

                pass
            case _:
                print(f"Tactic ({tactic}) is not a valid tactic!")

        results.append({
            "id": id,
            "found_id": found_id
        })

    return results

import simulation_handler


if __name__ == "__main__":
    simulation_handler.run_instances(
        amount=1000,
        boxes=30,
        # tactic="pick_at_random",
        tactic="follow_the_number_trail",
    )

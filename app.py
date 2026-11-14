import random
import sys
import time


def slow_print(text, delay=0.03):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()


def space_mission_simulator():
  slow_print(
      "\n=== COSMIC SENTINEL: SPACE MISSION DESIGN GAME ===", 0.02
  )
  slow_print(
      "Mission Objective: Design and launch a viable spacecraft within"
      " constraints.\n"
  )

  # Initial Resources
  budget = 100  # Millions USD
  mass_limit = 500  # kg
  power_limit = 200  # Watts

  current_mass = 0
  current_power_draw = 0
  selected_instruments = []

  # Component catalog: (Name, Cost ($M), Mass (kg), Power (W), Scientific Value)
  catalog = {
      1: ("High-Resolution Optical Camera", 30, 120, 50, 40),
      2: ("Infrared Spectrometer", 25, 90, 40, 35),
      3: ("Magnetometer", 15, 40, 15, 20),
      4: ("Ion Propulsion System", 35, 150, 80, 50),
      5: ("Standard Solar Array Panel", 20, 100, -120, 10),  # Generates power
      6: ("High-Gain Communication Dish", 15, 60, 30, 25),
  }

  while True:
    print(f"\n----------------UPLINK STATUS----------------")
    print(f" Remaining Budget: ${budget}M / $100M")
    print(
        f" Total Spacecraft Mass: {current_mass}kg / Max {mass_limit}kg"
        " (Limit Exceeds = Failure)"
    )
    print(
        f" Net Power Balance: {current_power_draw}W (Must be <= {power_limit}W"
        " generated)"
    )
    print(f" Selected Payloads/Systems: {len(selected_instruments)}")
    print("---------------------------------------------")
    print("Available Components to Add:")
    for key, item in catalog.items():
      print(
          f"  [{key}] {item[0]} -> Cost: ${item[1]}M | Mass: {item[2]}kg |"
          f" Power: {item[3]}W | Sci Value: {item[4]}"
      )

    print("  [9] Launch Mission!")
    print("  [0] Reset Configuration")
    print("  [X] Exit")

    choice = input("\nSelect an option (1-6, 9, 0, X): ").strip().upper()

    if choice == "X":
      print("Exiting simulator. Good luck!")
      break

    elif choice == "0":
      budget = 100
      current_mass = 0
      current_power_draw = 0
      selected_instruments = []
      print(" Configuration reset.")

    elif choice in ["1", "2", "3", "4", "5", "6"]:
      item_id = int(choice)
      item = catalog[item_id]

      if budget >= item[1]:
        budget -= item[1]
        current_mass += item[2]
        current_power_draw += item[3]
        selected_instruments.append(item[0])
        print(f" Added {item[0]} successfully!")
      else:
        print(" Error: Insufficient budget for this component!")

    elif choice == "9":
      slow_print(
          "\nInitiating pre-launch checks and physics simulation...", 0.04
      )
      time.sleep(1)

      # Validation checks
      failures = []
      if current_mass > mass_limit:
        failures.append(
            f"Mass overload! ({current_mass}kg > limit {mass_limit}kg)"
        )
      if current_power_draw > power_limit:
        failures.append(
            f"Power deficit! Net power required exceeds generation capacity."
        )
      if len(selected_instruments) == 0:
        failures.append("No instruments or systems selected!")

      if failures:
        print("\n MISSION FAILURE DURING LAUNCH SEQUENCE:")
        for f in failures:
          print(f" - {f}")
        print(
            "Tune your engineering trade-offs and try again next launch window!"
        )
      else:
        total_sci = sum([catalog[k][4] for k in [1, 2, 3, 4, 5, 6] if any])
        print("\n SUCCESS! LIFT-OFF SUCCESSFUL!")
        slow_print(
            "Your spacecraft has successfully cleared Earth's orbit and is"
            " heading toward its deep-space destination!"
        )
        print(f"Final Mission Scientific Score: {random.randint(85, 98)}/100")
        print(
            "Thank you for playing Cosmic Sentinel: Space Mission Design Game!"
        )
        break
    else:
      print("Invalid choice. Please pick from the menu.")


if __name__ == "__main__":
  space_mission_simulator()
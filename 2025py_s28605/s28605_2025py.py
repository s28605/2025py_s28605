# ------------------------------------------------------------
# Purpose: Generate a random DNA sequence in FASTA format,
#          inserting the user's name at a random position
#          (without affecting nucleotide statistics), save it
#          to a .fasta file, and display base composition.
# Context: Solution for Exercise 9 from Ex_9_EN.pdf
# ------------------------------------------------------------

import random

# ORIGINAL:
# (All script logic executed at top-level)
# MODIFIED (wrapped logic in main() function and added __name__ guard
#           for better modularity and to allow import without execution):
def get_positive_int(prompt):
    """
    Prompt repeatedly until the user enters a valid positive integer.
    """
    while True:
        try:
            # Read user input and attempt conversion to int
            value = int(input(prompt))
            # Reject non-positive integers
            if value <= 0:
                raise ValueError("must be > 0")
            return value
        except ValueError as e:
            # Notify user of invalid input and retry
            print(f"Invalid input ({e}), please enter a positive integer.")

def main():
    """
    Main program logic:
      1. Gather user inputs
      2. Generate random DNA sequence
      3. Insert user name
      4. Write to FASTA file (wrapped at 60 chars/line)
      5. Compute and display nucleotide statistics
    """

    # === User inputs ===

    # ORIGINAL:
    # length = int(input("Enter the sequence length: "))
    # MODIFIED (added input validation for positive integer):
    length = get_positive_int("Enter the sequence length (positive integer): ")

    seq_id = input("Enter the sequence ID: ").strip()
    description = input("Provide a description of the sequence: ").strip()
    user_name = input("Enter your name: ").strip()

    # === Sequence generation ===

    # Define allowed nucleotide characters
    nucleotides = ['A', 'C', 'G', 'T']

    # ORIGINAL:
    # sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    # MODIFIED (use random.choices for slightly better performance when k is known):
    sequence = ''.join(random.choices(nucleotides, k=length))

    # Choose a random insertion index between 0 and length (inclusive)
    position = random.randint(0, length)
    # Build the sequence with the user's name inserted
    sequence_with_name = sequence[:position] + user_name + sequence[position:]

    # === FASTA file writing ===

    file_name = f"{seq_id}.fasta"

    # ORIGINAL:
    # with open(file_name, 'w') as f:
    #     f.write(f">{seq_id} {description}\n")
    #     f.write(sequence_with_name + '\n')
    # MODIFIED (add error handling and wrap sequence at 60 characters per line):
    try:
        with open(file_name, 'w') as f:
            # Write FASTA header line
            f.write(f">{seq_id} {description}\n")
            # Write sequence lines, max 60 chars each for readability
            for i in range(0, len(sequence_with_name), 60):
                f.write(sequence_with_name[i:i+60] + "\n")
    except IOError as e:
        print(f"Error: Unable to write file '{file_name}': {e}")
        return

    # === Statistics calculation ===

    # Count each nucleotide in the original (unnamed) sequence
    counts = {nuc: sequence.count(nuc) for nuc in nucleotides}
    # Calculate percentage of each base
    percentages = {nuc: counts[nuc] / length * 100 for nuc in nucleotides}
    # Calculate combined C+G percentage
    cg_percent = (counts['C'] + counts['G']) / length * 100

    # === Output to user ===

    print(f"The sequence was saved to the file {file_name}")
    print("Sequence statistics:")
    for nuc in nucleotides:
        # Display each base percentage with one decimal
        print(f"{nuc}: {percentages[nuc]:.1f}%")
    # Display combined %CG
    print(f"%CG: {cg_percent:.1f}%")


if __name__ == "__main__":
    main()

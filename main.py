# GREEDY AL - BARANGAY REFLIEF PACKS
# Prompt user for total number of relief packs
num_of_reliefpacks = int(input("Enter total number of relif packs available: "))

# Prompt user for number of Barangays needing relief.
num_of_barangays = int(input("Enter number of Baragays: "))

# Declare list for Barangay information
barangays = []

# Prompt user for Barangay information
for i in range(num_of_barangays):

    # Prompt for Barangay Name
    name = input("Enter Barangay Name: ")

    # Prompt for number of families
    families = input("Enter number of families in Barangay ")

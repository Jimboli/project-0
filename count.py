# Get user input
text = input("Just copy it here: ")

# Initialize counters for each breed/category
australian_shepherd_count = 0
border_collie_count = 0
mixed_breed_count = 0
whippet_count = 0
labrador_retriever_count = 0
other_purebreed_count = 0

lines = text.split()

# Count occurrences of each breed/category
for line in lines:
    if "Australian" in line:
        australian_shepherd_count += 1
    if "Border" in line:
        border_collie_count += 1
    if "Mixed" in line:
        mixed_breed_count += 1
    if "Whippet" in line:
        whippet_count += 1
    if "Labrador" in line:
        labrador_retriever_count += 1
    if "Other" in line:
        other_purebreed_count += 1
    else:
        continue

# Print the counts
print(f"Australian Shepherd count: {100/45 * australian_shepherd_count}")
print(f"Border Collie count: {100/45 * border_collie_count}")
print(f"Mixed Breed count: {100/45 * mixed_breed_count}")
print(f"Whippet count: {100/45 * whippet_count}")
print(f"Labrador Retriever count: {100/45 * labrador_retriever_count}")
print(f"Other Purebreed count: {100/45 * other_purebreed_count}")

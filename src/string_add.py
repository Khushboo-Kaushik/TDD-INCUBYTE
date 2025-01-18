class Addclass:
    def add(self, numbers):
        # If the input is an empty string, return 0
        if not numbers:
            return 0
        
        # Handle the custom delimiter by checking if the string starts with "//"
        if numbers.startswith("//"):
            delimiter = numbers[2:numbers.index("\n")]
            numbers = numbers[numbers.index("\n")+1:]  # Remove the custom delimiter and new line
            numbers = numbers.replace(delimiter, ",")  # Replace the delimiter with a comma
        else:
            numbers = numbers.replace("\n", ",")  # Replace newlines with commas

        num_list = numbers.split(",")  # Split the string into a list of numbers

        # Check for negative numbers
        negatives = [num for num in num_list if int(num) < 0]
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(negatives)}")

        # Return the sum of all valid numbers
        return sum(map(int, num_list))

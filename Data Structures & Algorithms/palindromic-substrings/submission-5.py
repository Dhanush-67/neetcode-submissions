class Solution:
    def countSubstrings(self, s: str) -> int:
        def manacher(s):
            transformed = "#" + "#".join(s) + "#"
            n = len(transformed)

            radius = [0] * n

            left = 0
            right = 0

            for center in range(n):
                if center < right:
                    mirror = left + right - center

                    # Copy only the portion guaranteed to remain
                    # inside the known palindrome.
                    radius[center] = min(
                        radius[mirror],
                        right - center
                    )

                # Try to expand beyond what is already known.
                while (
                    center - radius[center] - 1 >= 0
                    and center + radius[center] + 1 < n
                    and transformed[center - radius[center] - 1]
                        == transformed[center + radius[center] + 1]
                ):
                    radius[center] += 1

                # Update the palindrome that reaches farthest right.
                if center + radius[center] > right:
                    left = center - radius[center]
                    right = center + radius[center]

            return radius

        radius = manacher(s)

        result = 0

        for value in radius:
            result += (value + 1) // 2

        return result
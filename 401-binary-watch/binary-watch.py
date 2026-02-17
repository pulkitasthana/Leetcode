class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        times = []
        
        # Iterate through all possible hours (0-11) and minutes (0-59)
        for h in range(12):
            for m in range(60):
                # Check if the sum of set bits equals the input turnedOn
                # bin(h).count('1') counts the number of 1s in the binary string
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    # Format the time:
                    # {h} handles the hour (no leading zero)
                    # {m:02d} handles the minute (pads with leading zero if needed)
                    times.append(f"{h}:{m:02d}")
                    
        return times
        
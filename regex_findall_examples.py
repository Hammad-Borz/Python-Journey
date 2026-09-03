import re
text = "I bought 23 apples, 12 bananas, and 33 oranges"
result = re.findall(r"\d+", text)
print(result)
text = """
Contact John at john@gmail.com
or Sarah at sarah@yahoo.com.
You can also email Ali at ali123@outlook.com.
"""
emails = re.findall( r"[\w.-]+@[\w.-]+\.\w+",
    text)
print(emails)

# All questions stored as dictionaries
questions = [
    {
        "question": "WHO WAS THE FIRST SERVING PRESIDENT OF INDIA?",
        "options": {
            "A": "DR ZAKIR HUSSAIN",
            "B": "K.R NARAYAN",
            "C": "RAJENDRA PRASAD",
            "D": "BHAIRON SING SHEKHAWAT"
        },
        "answer": "C",
        "reward": 70000
    },
    {
        "question": "WHO IS CALLED AS THE FATHER OF A.I. (ARTIFICIAL INTELLIGENCE)?",
        "options": {
            "A": "MARK WALLBERG",
            "B": "CILLIAN RAYAN",
            "C": "JOHN MCCARTHY",
            "D": "JIMMEL KIMMEL"
        },
        "answer": "C",
        "reward": 140000
    },
    {
        "question": "WHICH AMONG THE GIVEN WAS NAMED THE 49TH STATE OF UNITED STATES OF AMERICA?",
        "options": {
            "A": "ILLONOIS",
            "B": "ALASKA",
            "C": "CHICAGO",
            "D": "UTAH"
        },
        "answer": "B",
        "reward": 300000
    },
    {
        "question": "WHICH OF THESE COUNTRIES IS NOT PART OF BRICS ALLIANCE?",
        "options": {
            "A": "INDIA",
            "B": "RUSSIA",
            "C": "CHINA",
            "D": "AUSTRALIA"
        },
        "answer": "D",
        "reward": 750000
    },
    {
        "question": "CAPITAL CITY OF HARYANA IS?",
        "options": {
            "A": "CHANDIGARH",
            "B": "SONIPAT",
            "C": "GURUGRAM",
            "D": "FARIDABAD"
        },
        "answer": "A",
        "reward": 2000000
    },
    {
        "question": "THE OLDEST TRADE ROUTE IN THE HISTORY OF CIVILIZATION WAS?",
        "options": {
            "A": "SILK ROUTE",
            "B": "TEA HOUSE ROAD",
            "C": "ROYAL ROAD",
            "D": "INCENSE ROUTE"
        },
        "answer": "A",
        "reward": 5000000
    },
    {
        "question": "THE FIRST CALCULATOR IN THE HISTORY OF MANKIND WAS GIVEN BY WHICH SCIENTIST?",
        "options": {
            "A": "ALAN TURING",
            "B": "CHARLES BABBAGE",
            "C": "BLAISE PASCAL",
            "D": "THOMAS EDISON"
        },
        "answer": "C",
        "reward": 25000000
    },
    {
        "question": "THE FIRST EVER COMPUTER DEVICE TO DECYPHER GERMAN CODES DURING WWII WAS INVENTED IN WHICH YEAR?",
        "options": {
            "A": "1940s",
            "B": "1930s-1940s",
            "C": "1920s",
            "D": "1830s"
        },
        "answer": "A",
        "reward": 50000000
    },
    {
        "question": "THE LONGEST RIVER IN INDIA IS?",
        "options": {
            "A": "CHENAB",
            "B": "GANGA",
            "C": "SUTLEJ",
            "D": "INDUS"
        },
        "answer": "B",
        "reward": 100000000
    },
    {
        "question": "THE 'DIRECT ACTION DAY' IS ASSOCIATED WITH INDIAN INDEPENDENCE HISTORY. WHICH DATE WAS IT?",
        "options": {
            "A": "10 JUNE 1946",
            "B": "18 JULY 1947",
            "C": "20 FEBRUARY 1947",
            "D": "16 AUGUST 1946"
        },
        "answer": "D",
        "reward": 216440000
    }
]

# Track cumulative prize
total_prize = 0  

# Loop through each question with number
for idx, q in enumerate(questions, start=1):
    print(f"\nQ{idx}: {q['question']}")
    for key, value in q["options"].items():
        print(f"{key}. {value}")
    
    answer = input("Your Answer: ").strip().upper()

    if answer == q["answer"]:
        total_prize += q["reward"]
        print(f"✅ Correct! You won Rs {q['reward']} for this question.")
        print(f"💰 Total Prize so far: Rs {total_prize}")
    else:
        print("❌ WRONG! GAME OVER.")
        print(f"🏆 You take home Rs {total_prize}")
        exit()

print("\n🎉 Congratulations! You cleared all questions!")
print(f"Final Winnings: Rs {total_prize}")

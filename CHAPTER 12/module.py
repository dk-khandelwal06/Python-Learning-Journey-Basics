def myFunc():
    print("Hello World")



if __name__ == "__main__":
    # If this code is directly executed by running the file its present in
    print("We are directly running this code")
    myFunc()

    # Agar jis file me run kar rahe to main likha aayega yani main file par kahin aur ise import kar rahe to iska naam likha aayeg !! Check 08_main.py
    print(__name__)
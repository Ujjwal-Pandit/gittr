{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOswVYwmKNTVabIqBVDgje7",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ujjwal-Pandit/gittr/blob/main/Zybook%206.10%20Ch%206%20Program%3A%20Authoring%20assistant%20(Python%203).py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Fej99FktTEJf"
      },
      "source": [
        "# Use islower()\n",
        "# USe isupper()\n",
        "# Create string concatenation to make changes to the strings. \n",
        "# Implement fix_capitalization function\n",
        "# Lowercase letter at the beginning to be capitalized\n",
        "# Also return the number of letters that has been capitalized.\n",
        "# Call fix_capitalization in the print_menu() function, then output the number of letter capitalized and the edited string.\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VN2UM3Z_cLQ1"
      },
      "source": [
        "def print_menu():\n",
        "    print('MENU\\nc - Number of non-whitespace characters\\nw - Number of words\\nf - Fix capitalization\\nr - Replace punctuation\\ns - Shorten spaces\\nq - Quit\\n')\n",
        "    menuOp = input('Choose an option:')\n",
        "    while (menuOp != 'c' and menuOp != 'w' and menuOp != 'f' and menuOp != 'r' and menuOp != 's' and menuOp != 'q'):\n",
        "        menuOp = input('Choose an option:')\n",
        "    return menuOp\n",
        "\n",
        "\n",
        "def get_num_of_non_WS_characters(inputStr):\n",
        "    whitespace = 0\n",
        "    for character in inputStr:\n",
        "        if(character == ' ' or character == '\\t'):\n",
        "            whitespace += 1\n",
        "    return (len(inputStr) - whitespace)\n",
        "\n",
        "\n",
        "def get_num_of_words(inputStr):\n",
        "    words = inputStr.split()\n",
        "    \n",
        "    return len(words)\n",
        "\n",
        "\n",
        "def fix_capitalization(inputStr):\n",
        "    letCapped = 0\n",
        "    charArray = []\n",
        "    for character in inputStr:\n",
        "        charArray.append(character)\n",
        "   \n",
        "    if(charArray[0].islower()):\n",
        "        charArray[0] = inputStr[0].upper()\n",
        "        letCapped += 1\n",
        "\n",
        "   \n",
        "    x = 0\n",
        "    capNext = 'false'\n",
        "    for character in charArray:\n",
        "        if(capNext == 'true' and character != ' ' and character != '\\t'):\n",
        "            charArray[x] = inputStr[x].upper()\n",
        "            letCapped += 1\n",
        "            capNext = 'false'\n",
        "        if(character == '.' or character == '!' or character == '?'):\n",
        "            capNext = 'true'\n",
        "        x += 1\n",
        "\n",
        "    \n",
        "    newString = ''\n",
        "    for character in charArray:\n",
        "        newString = newString + character\n",
        "\n",
        "    print('Number of letters capitalized:', letCapped, end = '\\n')\n",
        "    print('Edited text:', newString, end='\\n\\n')\n",
        "    return newString, letCapped\n",
        "\n",
        "\n",
        "def replace_punctuation(inputStr, exclamationCount, semicolonCount):\n",
        "    exclamationCount = 0\n",
        "    semicolonCount = 0\n",
        "    charArray = []\n",
        "    for character in inputStr:\n",
        "        charArray.append(character)\n",
        "       \n",
        "   \n",
        "    x = 0\n",
        "    for character in charArray:\n",
        "        if(character == '!'):\n",
        "            charArray[x] = '.'\n",
        "            exclamationCount += 1\n",
        "        elif(character == ';'):\n",
        "            charArray[x] = ','\n",
        "            semicolonCount += 1\n",
        "        x += 1\n",
        "\n",
        "    \n",
        "    newString = ''\n",
        "    for character in charArray:\n",
        "        newString = newString + character\n",
        "\n",
        "    \n",
        "    print('Punctuation replaced', end = '\\n')\n",
        "    print('exclamationCount:', exclamationCount, end='\\n')\n",
        "    print('semicolonCount:', semicolonCount, end='\\n')\n",
        "    print('Edited text:', newString, end='\\n\\n')\n",
        "    return newString\n",
        "\n",
        "\n",
        "def shorten_space(inputStr):\n",
        "    words = inputStr.split()\n",
        "    newString = ''\n",
        "    for word in words:\n",
        "        if newString == '':\n",
        "            newString = word;\n",
        "        elif (newString != ''):\n",
        "            newString = newString + ' ' + word\n",
        "    print('Edited text:', newString, end='\\n\\n')\n",
        "    return newString\n",
        "\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    \n",
        "    inputStr = str(input('Enter a sample text:\\n'))\n",
        "    print('\\nYou entered:', inputStr, end='\\n\\n')\n",
        "    command = ''\n",
        "    while(command != 'q'):\n",
        "        command = print_menu()\n",
        "        if (command == 'c'):\n",
        "            \n",
        "            print('Number of non-whitespace characters:', get_num_of_non_WS_characters(inputStr), end='\\n\\n')\n",
        "        elif (command == 'w'):\n",
        "            \n",
        "            print('Number of words:', get_num_of_words(inputStr), end = '\\n\\n')\n",
        "        elif (command == 'f'):\n",
        "            \n",
        "            fix_capitalization(inputStr)\n",
        "        elif (command == 'r'):\n",
        "            \n",
        "            replace_punctuation(inputStr, 0, 0)\n",
        "        elif (command == 's'):\n",
        "            \n",
        "            shorten_space(inputStr)\n",
        "        else:\n",
        "            print(\"\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "trc9WEyLe9hg"
      },
      "source": [
        "def print_menu():\n",
        "    print('MENU\\nc - Number of non-whitespace characters\\nw - Number of words\\nf - Fix capitalization\\nr - Replace punctuation\\ns - Shorten spaces\\nq - Quit\\n')\n",
        "    menuOp = input('Choose an option:')\n",
        "    while (menuOp != 'c' and menuOp != 'w' and menuOp != 'f' and menuOp != 'r' and menuOp != 's' and menuOp != 'q'):\n",
        "        menuOp = input('Choose an option:')\n",
        "    return menuOp"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bi4hahe9g1DT"
      },
      "source": [
        "A print_menu function is defined which prints the menu that is given pre-defined. Now, according to the question, when we should give option to the customer whether he wants to choose which option, the customer may decline the order in the first run itself, and we should regularly ask for another option if he chooses one until he declines. So, while loop works best here. Also the point to notice is that if user uses another text not from the menu, we should regularly ask for option. So, instead of defining like while menuOp == options from menu, what we should do is use while loop when menuOp != to any of the option in menu, reask for input."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ANF_MYjRfBCO"
      },
      "source": [
        "def get_num_of_non_WS_characters(inputStr):\n",
        "    whitespace = 0\n",
        "    for character in inputStr:\n",
        "        if(character == ' ' or character == '\\t'):\n",
        "            whitespace += 1\n",
        "    return (len(inputStr) - whitespace)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qhjyGYxgf_KZ"
      },
      "source": [
        "A function get_num_of_non_WS_characters is defined. What I have done here is used for loop to skim out all the whitespaces and tab. The thing is to note that after the skimming of all whitespace characters, we subtract the whitespace characters from total characters to get total non whitespaced characters. There are many ways to do it, like we could even use len to count the length of all characters after removal of whitespaces."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AUVWtBUffXYF"
      },
      "source": [
        "def get_num_of_words(inputStr):\n",
        "    words = inputStr.split()\n",
        "    \n",
        "    return len(words)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UouR74DmiAAE"
      },
      "source": [
        "The easiest of all is to count the number of words in the input text. The best is to split the words after spaces and count all words using the len."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YtOrGhoJfY_N"
      },
      "source": [
        "def fix_capitalization(inputStr):\n",
        "    letCapped = 0\n",
        "    charArray = []\n",
        "    for character in inputStr:\n",
        "        charArray.append(character)\n",
        "   \n",
        "    if(charArray[0].islower()):\n",
        "        charArray[0] = inputStr[0].upper()\n",
        "        letCapped += 1\n",
        "\n",
        "   \n",
        "    x = 0\n",
        "    capNext = 'false'\n",
        "    for character in charArray:\n",
        "        if(capNext == 'true' and character != ' ' and character != '\\t'):\n",
        "            charArray[x] = inputStr[x].upper()\n",
        "            letCapped += 1\n",
        "            capNext = 'false'\n",
        "        if(character == '.' or character == '!' or character == '?'):\n",
        "            capNext = 'true'\n",
        "        x += 1\n",
        "\n",
        "    \n",
        "    newString = ''\n",
        "    for character in charArray:\n",
        "        newString = newString + character\n",
        "\n",
        "    print('Number of letters capitalized:', letCapped, end = '\\n')\n",
        "    print('Edited text:', newString, end='\\n\\n')\n",
        "    return newString, letCapped"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UBAV5pp02BqM"
      },
      "source": [
        "This is the copied code from the internet which I will explain later after going through the code in free time. I need to study first bool and append methods before understanding everything clearly."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kDmsM517fkaP"
      },
      "source": [
        "def replace_punctuation(inputStr, exclamationCount, semicolonCount):\n",
        "    exclamationCount = 0\n",
        "    semicolonCount = 0\n",
        "    charArray = []\n",
        "    for character in inputStr:\n",
        "        charArray.append(character)\n",
        "       \n",
        "   \n",
        "    x = 0\n",
        "    for character in charArray:\n",
        "        if(character == '!'):\n",
        "            charArray[x] = '.'\n",
        "            exclamationCount += 1\n",
        "        elif(character == ';'):\n",
        "            charArray[x] = ','\n",
        "            semicolonCount += 1\n",
        "        x += 1\n",
        "\n",
        "    \n",
        "    newString = ''\n",
        "    for character in charArray:\n",
        "        newString = newString + character\n",
        "\n",
        "    \n",
        "    print('Punctuation replaced', end = '\\n')\n",
        "    print('exclamationCount:', exclamationCount, end='\\n')\n",
        "    print('semicolonCount:', semicolonCount, end='\\n')\n",
        "    print('Edited text:', newString, end='\\n\\n')\n",
        "    return newString"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-UfbBnemxvBB"
      },
      "source": [
        "This is simple, here we first turn the sentences into a string container, so that we can modify without modifying the original sentence. We use for loop to go through each character and replace all '!' with '.' and ';' with ',', also we count the total exclamations and semicolons by placing counter inside the loop. And we finally convert the string from container into the new string statement using for loop. We finally print everything according to question."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9SufIDgYfxjY"
      },
      "source": [
        "def shorten_space(inputStr):\n",
        "    words = inputStr.split()\n",
        "    newString = ''\n",
        "    for word in words:\n",
        "        if newString == '':\n",
        "            newString = word;\n",
        "        elif (newString != ''):\n",
        "            newString = newString + ' ' + word\n",
        "    print('Edited text:', newString, end='\\n\\n')\n",
        "    return newString"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6F_KJ9P-0k_s"
      },
      "source": [
        "Here a function shorten_space is defined. Here we are instructed to reduce the whitespace if more than one space exists. The best way is to split the words first using .split(), which only takes the non white space characters and place them into a list. Then we can add for loop to loop through each word in a container to add space between the words."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iZSnKRnvf24e"
      },
      "source": [
        "if __name__ == '__main__':\n",
        "    \n",
        "    inputStr = str(input('Enter a sample text:\\n'))\n",
        "    print('\\nYou entered:', inputStr, end='\\n\\n')\n",
        "    command = ''\n",
        "    while(command != 'q'):\n",
        "        command = print_menu()\n",
        "        if (command == 'c'):\n",
        "            \n",
        "            print('Number of non-whitespace characters:', get_num_of_non_WS_characters(inputStr), end='\\n\\n')\n",
        "        elif (command == 'w'):\n",
        "            \n",
        "            print('Number of words:', get_num_of_words(inputStr), end = '\\n\\n')\n",
        "        elif (command == 'f'):\n",
        "            \n",
        "            fix_capitalization(inputStr)\n",
        "        elif (command == 'r'):\n",
        "            \n",
        "            replace_punctuation(inputStr, 0, 0)\n",
        "        elif (command == 's'):\n",
        "            \n",
        "            shorten_space(inputStr)\n",
        "        else:\n",
        "            print(\"\")"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
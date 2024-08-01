#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_PARAGRAPH_LENGTH 1000
#define MAX_WORD_LENGTH 50
#define MAX_WORDS 100

typedef struct {
    char word[MAX_WORD_LENGTH];
    int count;
} WordFreq;

void toLowerCase(char *str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

int findWord(WordFreq words[], int wordCount, char *word) {
    for (int i = 0; i < wordCount; i++) {
        if (strcmp(words[i].word, word) == 0) {
            return i;
        }
    }
    return -1;
}

int main() {
    char paragraph[MAX_PARAGRAPH_LENGTH];
    WordFreq words[MAX_WORDS];
    int wordCount = 0;

    printf("Enter a paragraph: ");
    fgets(paragraph, MAX_PARAGRAPH_LENGTH, stdin);

    char *token = strtok(paragraph, " ,.-\n");
    while (token != NULL) {
        toLowerCase(token);
        int index = findWord(words, wordCount, token);

        if (index == -1) {
            strcpy(words[wordCount].word, token);
            words[wordCount].count = 1;
            wordCount++;
        } else {
            words[index].count++;
        }

        token = strtok(NULL, " ,.-\n");
    }

    printf("Word Frequencies:\n");
    for (int i = 0; i < wordCount; i++) {
        printf("%s: %d\n", words[i].word, words[i].count);
    }

    return 0;
}

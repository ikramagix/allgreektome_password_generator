import { wordList } from './words';

class PasswordGenerator {
    readonly passwordLength: number;

    /**
     * Creates a new PasswordGenerator instance.
     * @param length - The desired length of the generated password.
     */
    constructor(length: number) {
        this.passwordLength = length;
    }

    /**
     * Generates a password consisting of random characters.
     * @returns A string representing the generated password.
     */
    public generatePassword(): string {
        let password = '';
        while (password.length < this.passwordLength) {
            if (Math.random() > 0.5) {
                // Add a random character
                password += this.generateRandomCharacter();
            } else {
                // Add a whole word (or part of it)
                const word = this.getRandomItem(wordList);
                password += word;
            }
        }
        return password.slice(0, this.passwordLength);
    }


    /**
     * Generates a single random character from the wordList.
     * Randomly converts the character to uppercase about half the time.
     * @returns A single character string.
     */

    private generateRandomCharacter(): string {
        // Pick a random word from wordList
        const randomWord = this.getRandomItem(wordList);
        // Pick a random character from that word
        const randomChar = randomWord.charAt(Math.floor(Math.random() * randomWord.length));
        // Randomly uppercase about half the time
        if (Math.random() > 0.5) {
            return randomChar.toUpperCase();
        }
        return randomChar;
    }


    /**
     * Selects a random item from the provided array.
     * @param array - An array of strings to pick from.
     * @returns A randomly selected string from the array.
     */
    protected getRandomItem(array: string[]): string {
        const randomIndex = Math.floor(Math.random() * array.length);
        return array[randomIndex];
    }
}

class ReadablePasswordGenerator extends PasswordGenerator {
    /**
     * Generates a random word from the wordList.
     * @returns A single word string.
     */
    private generateRandomWord(): string {
        return this.getRandomItem(wordList);
    }

    /**
     * Generates a readable password consisting of words joined by hyphens.
     * The password length is at least the specified passwordLength.
     * @returns A string representing the generated readable password.
     */
    public generatePassword(): string {
        let password = '';
        // Keep adding words separated by '-' until reaching desired length
        while (password.length < this.passwordLength) {
            const word = this.generateRandomWord();
            if (password.length === 0) {
                password += word;
            } else {
                password += '-' + word;
            }
        }
        // Trim the password to the exact requested length if it exceeds it
        return password.slice(0, this.passwordLength);
    }
}

// Example 1: Standard random character password based on wordList
const myPasswordGenerator = new PasswordGenerator(15);
const password = myPasswordGenerator.generatePassword();
console.log('Generated (random) password:');
console.log(password);

// Example 2: Pseudo-readable password extracted from wordList
const readablePasswordGenerator = new ReadablePasswordGenerator(75);
const readablePassword = readablePasswordGenerator.generatePassword();
console.log('\nGenerated (readable) password:');
console.log(readablePassword);

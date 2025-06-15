# AllGreekToMe - Password Generator Template

You can use this as a lightweight, beginner-friendly TypeScript template for experimenting with password generation using class-based design. 

It includes:
- A base `PasswordGenerator` class
- An extendable `ReadablePasswordGenerator` class using pseudo-Greek words
- A Python script to generate fake but plausible Greek-style words
- Modular setup with `tsconfig.json` and clean output to `/dist`

It generates two types of pseudo-"readable" passwords based on a list of fake Greek-inspired words:

- A **random character combination password**, where characters are randomly sampled from the pseudo-Greek word list and combined into a password of the desired length.
- A **pseudo-readable password**, where whole fake Greek-style words from the list are concatenated with hyphens to form a more readable, phrase-like password.

This is a small practice project for refreshing TypeScript skills. The goal was to explore TypeScript classes, visibility modifiers (`public`, `private`, `protected`), inheritance, and basic file structure. 

It also includes a Python script to generate pseudo-Greek words and a TypeScript class to construct fake passwords from them. 

## Structure

```
.
├── README.md                # Project information
├── greek-words-generator.py # Python script that generates 500 pseudo-Greek words into words.ts
├── index.ts                 # TypeScript logic for password generation
├── tsconfig.json            # TypeScript configuration
└── words.ts                 # List of Greek-style synthetic words

````

## Usage

### 1. Refresh word list (Optional)

The generated words are **synthetic**, inspired by real Greek morphology but semantically meaningless. Run the Python script to (re)generate 500 fake Greek-looking words:

```bash

python3 greek-words-generator.py
````

This will overwrite `words.ts` with a fresh list in the correct export format.

### 2. Compile & run the generator

Use the TypeScript compiler and Node.js to generate a password:

```bash
tsc
node index.js
```

### 3. Output

You will see two passwords in the following formats:

```
Generated (random) password:
algopaniscopoih

Generated (readable) password:
neurophiloautochronoplastikon-cryptognosomorphogenesis-psychoautognomonikon
```

> [!IMPORTANT]
> Don't use this as it is to generate passwords. <br>
> Don't open an issue because you've been hacked after using this. <br>
> Don't either if you've bankrupted after using this code thinking it's a legitimate password generator for your vibe coder SaaS. <br>
> 
> ![Stranger Danger GIF](https://c.tenor.com/Tse7j6gwTCwAAAAC/tenor.gif)
>
> Don't use it in production. Don't use it in development.
> Use it to have fun and/or maybe learn one thing or two about TypeScript classes and/or as a base for more complex projects. <br>
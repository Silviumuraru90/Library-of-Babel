# Library of Babel - A variation from Jorge Luis Borges's idea

![Library of Babel](Media/Library.png)


## Interesting facts?

To begin with, [this document](https://libraryofbabel.info/Borges/KurdLasswitz-TheUniversalLibrary.pdf). This will give you an idea why even this "short" variation cannot be processed by a personal PC and why not even sites like [this](https://libraryofbabel.info/theory4.html) don't store the information, but make it so real that you would believe the opposite. In any case, what they achieved is truly remarkable!


The `cure for cancer` should be found within the output lines. Probability? Well, `100%`. 

What else? Well:
- all your `dreams`, `hopes`, `feelings`, `ideas`;
- the `secrets of the universe`;
- even `your own future`;

## What is it?

It's a collection of `Books` (folders), thus `Pages` (files), that contain on each `Line` a variation of chars. 

## How to use it?

You can run the provided `library_of_babel.py` script for single-core processing or either of `async_events.py` or `process_pool.py`, which are the parallel processing variations. You'll surely need a lot of disk and RAM to complete the output.

My recommendation for lengthy char combos is to run any of the parallel processing scripts as it is (You'll notice it will create folders with a number and the letter `A` in the names and also files with letter `a` next to the number) and then modify the script to output folders and files with letter `B` & `b` respectively, while also reversing the char sequence provided (letters + " ") and have this second script run in parallel on a different PC. This way, the first script will start creating the combinations from one end, while the other from the other end and you can stop both when you saw they surely outputed the same block of chars (can be easily figured out if you also print to the CLI the current char-combo). It's most probably not going to be the middle, as PCs might be different in RAM and CPU characteristics. One important thing to notice is that each script with generate at first the combos for lengths of `n-(n-1)`, `n-(n-2)` and so on, until `n-1`. These will have duplicates when both apparent halfs of the libs will be combined (`A`s and `B`s), so this works only for combos of `length=n`, which means there is a `len(combo) != max_length` that will need to be added as a filter, in order to generate only the neccesary ones and then combine the files from both PCs into one. This will also work only for 1 run only, otherwise folder and file names will be once again generated from the start, with `1A`, `1B`, `1a`, `1b`... Perhaps their names are better to contain a random string at generation, with low probability to repeat itself, something like [the function used here](https://gitlab.com/Silviu_space/rybka/-/blob/756eca44717aada4d3085243a9c5e15d1464071f/core.py#L58).

=> but with more than 10 chars in length;

---


In an attempt to make this run even on a personal PC, initially (with combos of length up to `10`), there are some limitations imposed to the output, hence there will be no combos that:
- contain the same letter 3 times one after the other;
- contain the same letter 6 times in any substring throughout the variation itself;
- contain specific char constructs of 2, 3 or 4 letters that would never appear in an English word (avoiding names and onomatopoeias);
- contain less than 5 distinct chars for a length or combo of between 10-20 chars;
- contain less than 8 distinct chars for a length or combo of over 20 chars;
- contain specific 2-char variation at the beginning of the combo;
- contain no doubling letters, such as `aa` or `bb` or so on, as a standalone (delimited by spaces / endlines) structure;
- contain no other char formations other than valid 2 letter or 3 letter English words, as long as such char group in a combination, avoiding spaces at this char group's ends, is 2 or 3 in length; 
- contain no 4-letter progressions such as `abcd`, `klmn` or others, no matter if coming in the form of a substring or at a `step` of indices within the combo (the step is big enough to assure a 4-char progression within a 27-char length limit). This means that the following constructs are avoided: `aadefgaa`, `aadaeafag`, but also the inverse situation, such as `gfed` or `aaan    m  d ldwwak`;
- contain no two spaces one next to the other;
- contain words that have no vowels and are over 6 chars in length, with the exception of "rhythms" (the longest one in English lang.);
- contain words that have no consonants and are over 5 chars in length, with the exception of "euouae" (the longest one in English lang.); `Definition: euouae (juːˈuːiː ) noun. music. (in medieval music) a mnemonic used to recall the sequence of tones in a particular passage of the Gloria Patri.` => Per <b>Collins English Dictionary</b>. While, per <b>Wikipedia</b>: `The "Gloria Patri", also known as the "Glory Be to the Father" or, colloquially, the "Glory Be", is a doxology, a short hymn of praise to God in various Christian liturgies`.

But you can tweak it your way. The `27` combination number matches the number of chars used (English alphabet + the space char), but it can be edited into whichever string length you would want. Any value above `10` will be a bit too much for a personal PC to process, still you can set just a value like `4`, let's say, which won't take much t genrate, or above `50` and the more length you add, the more sentences it will be able to export, until having the solution to everything in this world.

Use the `search.exe` software to find strings up to your imposed N-char limit (27 as a default, but actually this limit is not logically related to the nr. of chars in English alphabet + the space char, is just a mere default that simbolizes that) and see where were those found. `Search and see where they'll be present, in the depths of such Library`.

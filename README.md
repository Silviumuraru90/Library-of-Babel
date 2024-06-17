# Library of Babel - A variation from Jorge Luis Borges's idea

![Library of Babel](Media/Library.png)

## Interesting facts?

 The `cure for cancer` should be found within those lines. Probability? Well, `100%`. Even if not found entirely within the same line or page or book, it should still be there.

 What else? Well:
- all your `dreams`, `hopes`, `feelings`, `ideas`;
- the `secrets of the universe`;
- even `your own future`;

## What is it?

It's a collection of `Books` (folders), thus `Pages` (files), that contain on each `Line` a variation of chars. 

## How to use it?

You can either <b>download</b> the whole repo of files (the `Library` folder) or <b>generate</b> it, via the provided `library_of_babel.py` script. Make sure to have at least `` GB free on the disk where you'll be running this script.

Then, the beauty of it arises from the fact that whatever string up to a length of `27` chars should be found on a specific `Line` of a `Page` in a `Book`, considering the following limitations - combinations of chars in this book are created in such a way that there are generated enough variations  to include `the whole English alphabet (and by this quite possible many others)`, but restrictive enough in order to make such script be able to be generated on a personal PC and also stored in a free manner in Cloud (speaking of processing, but especially of disk space), hence there are no combos that:
- contain the same letter 3 times one after the other;
- contain the same letter 6 times in any substring throughout the variation itself;
- contain specific char constructs of 2, 3 or 4 letters that would never appear in an English word (avoiding names and onomatopoeias);
- contain less than 5 distinct chars for a length or combo of between 10-20 chars;
- contain less than 8 distinct chars for a length or combo of over 20 chars;
- contain specific 2-char variation at the beginning of the combo;
- contain no 4-letter progressions such as `abcd`, `klmn` or others, no matter if coming in the form of a substring or at a `step` of indices within the combo (the step is big enough to assure a 4-char progression within a 27-char length limit). This means that the following constructs are avoided: `aadefgaa`, `aadaeafag`, but also the inverse situation, such as `gfed` or `aaan    m  d ldwwak`;
- contain no two spaces one next to the other;
- contain words that have no vowels and are over 6 chars in length, with the exception of "rhythms" (the longest one in English lang.);
- contain words that have no consonants and are over 5 chars in length, with the exception of "euouae" (the longest one in English lang.); `Definition: euouae (juːˈuːiː ) noun. music. (in medieval music) a mnemonic used to recall the sequence of tones in a particular passage of the Gloria Patri.` => Per <b>Collins English Dictionary</b>. While, per <b>Wikipedia</b>: `The "Gloria Patri", also known as the "Glory Be to the Father" or, colloquially, the "Glory Be", is a doxology, a short hymn of praise to God in various Christian liturgies`.

Use the `search.exe` software to find strings up to a 27-char limit and see where were those found. `They are NOT generated on the spot, but already present, somewhere, in the depths of such Library`.

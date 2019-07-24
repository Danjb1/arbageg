# arbageg

A simple program that turns text into gibberish by applying some offset to the positions of the characters in each word, thus changing the starting letter.

It uses simple rules to determine the "best" offset for each word.

## Example

### Before

    Once you beat the big badasses and clean out the moon base you're supposed
    to win, aren't you? Aren't you? Where's your fat reward and ticket home?
    What the hell is this? It's not supposed to end this way! It stinks like
    rotten meat, but looks like the lost Deimos base. Looks like you're stuck on
    the shores of hell. The only way out is through.

### After

    Nceo ouy atbe het gbi adassesb nda leanc uto het oonm aseb ou'rey upposeds
    ot inw, ren'ta ouy? Ren'ta ouy? Here'sw oury atf drewar nda ettick meho?
    Hatw het lhel si hist? 'Sit otn upposeds ot nde hist ayw! Ti tinkss ikel
    ottenr atme, tbu slook ikel het tlos Eimosd aseb. Slook ikel ou'rey tucks no
    het horess fo lhel. Het lyon ayw uto si oughthr.

## Run

    python arbageg.py "Hello world!"

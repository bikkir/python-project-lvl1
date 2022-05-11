#!/usr/bin/env python
import brain_games.greet
import brain_games.even_check

def main():
    i = 0
    if brain_games.even_check.sol is True and i < 3:
        brain_games.even_check.check()
        i += 1
    else:
        exit




if __name__ == '__main__':
    main()

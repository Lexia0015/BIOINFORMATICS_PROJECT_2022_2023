#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'


def transcription(sequence:str) -> str:
    if "T" in sequence:
        sequence_ARN = sequence.replace("T", "U")
    return sequence_ARN

def traduction():
    pass


if __name__ == '__main__':
    print(transcription("ATCGACGTAGC"))
    traduction()
'''
Project-wide utilities.
'''

from copy import deepcopy


def strip_to_melody(sequence):
    '''
    Strip a NoteSequence of everything except the melody.

    Parameters
    ----------
    sequence : NoteSequence
        The input sequence.

    Returns
    -------
    NoteSequence
        The input sequence's melody as a NoteSequence.
    '''
    melody = deepcopy(sequence)
    melody_notes = list(filter(lambda note: not note.instrument,
                               sequence.notes[:]))
    del melody.notes[:]
    melody.notes.extend(melody_notes)
    return melody


def remove_melody(sequence):
    '''
    Strip a NoteSequence of the melody.

    Parameters
    ----------
    sequence : NoteSequence
        The input sequence.

    Returns
    -------
    NoteSequence
        The input sequence's non-melody as a NoteSequence.
    '''
    not_melody = deepcopy(sequence)
    not_melody_notes = list(filter(lambda note: note.instrument,
                                   sequence.notes[:]))
    del not_melody.notes[:]
    not_melody.notes.extend(not_melody_notes)
    return not_melody

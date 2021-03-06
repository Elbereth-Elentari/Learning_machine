# Learning_machine

A basic python 3.6.5 program for memorising any kind of vocabulary, or simple answers to questions. The questions in the two csv files are about basic python functions.

<img src="https://myheritagelanguage.com/wp-content/uploads/2017/12/B5_P20a.jpg">*

Start with a 3-column CSV (no header), with 20 rows. Call it "flashcards.csv" (or change the name at the top of the program).<br>
Column 0: the questions (e.g. the meaning of the word you want to memorise).<br>
Column 1: the answer (e.g. the word you want to memorise).<br>
Column 2: 0 (the initial level of this question in the algorithm).

The program moves questions between 5 boxes of increasing size.<br>
Box 0 contains just 20 places for questions - that's the initial box for all questions.<br>
Box 1 contains 30 places.<br>
Box 2 - 45.<br>
Box 3 - 68.<br>
Box 4 - 101 - this is the final box.

If you answer a question correctly, its level is increased by 1 (it's "moved" to a higher box). If not, it stays on the same level.<br>
Once a higher box is full, you start answering questions from that higher box.<br>
Once you finish with the higher box, you go back to whichever level is full, or to level 0.

At the end you will get statists of how many questions are left at each level. Make sure that you fill in level 0 each time so that you finish with 20 questions at this level. This regular refilling is educational. So don't start with a complete list of 2,000 questions at level 0 - it'll be difficult to ever get to level 1 with them, because the program randomises the question list during every session.

The session is limited to showing you 50 questions in total, regardless of their levels. Don't do more than one session at a time. You have to let your brain forget and learn again - that's super effective!

*<a href="https://myheritagelanguage.com/book/teaching-learning-strategies-techniques/part-learning-strategies-techniques-different-sub-areas/techniques-strategies-practicing-general-m1-4/m4-flashcards-useful-aid-learning-professionals/">Image source</a>.

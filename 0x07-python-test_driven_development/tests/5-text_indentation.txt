The ``5-`text_indentation` module
======================

Using ``text_indentation``
-------------------

Importing the function from the module:
	>>> text_indentation = __import__("5-text_indentation").text_indentation

Checking for module docstring:
	 >>> m = __import__("5-text_indentation").__doc__
	 >>> len(m) > 1
	 True

Checking for function docstring:
	 >>> f = __import__("5-text_indentation").text_indentation.__doc__
         >>> len(f) > 1
         True

Checking for no args:
	 >>> text_indentation()
	 Traceback (most recent call last):
	 ...
	 TypeError: text_indentation() missing 1 required positional argument: 'text'

Checking for too many args:
	 >>> text_indentation("Hello", "Hi")
	 Traceback (most recent call last):
	 ...
	 TypeError: text_indentation() takes 1 positional argument but 2 were given

Checking for passing None:
	 >>> text_indentation(None)
	 Traceback (most recent call last):
	 ...
	 TypeError: text must be a string

Checking for passing non-string type:
	 >>> text_indentation(1)
         Traceback (most recent call last):
         ...
         TypeError: text must be a string

Checking for endingin special char:
	 >>> text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres.""")
	 Lorem ipsum dolor sit amet, consectetur adipiscing elit.
	 <BLANKLINE> 
	 Quonam modo?
	 <BLANKLINE>
	 Utrum igitur tibi litteram videor an totas paginas commovere?
	 <BLANKLINE>
	 Non autem hoc:
	 <BLANKLINE>
	 igitur ne illud quidem.
	 <BLANKLINE>
	 Fortasse id optimum, sed ubi illud:
	 <BLANKLINE>
	 Plus semper voluptatis?
	 <BLANKLINE>
	 Teneo, inquit, finem illi videri nihil dolere.
	 <BLANKLINE>
	 Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.
	 <BLANKLINE>
	 Si id dicis, vicimus.
	 <BLANKLINE>
	 Inde sermone vario sex illa a Dipylo stadia confecimus.
	 <BLANKLINE>
	 Sin aliud quid voles, postea.
	 <BLANKLINE>
	 Quae animi affectio suum cuique tribuens atque hanc, quam dico.
	 <BLANKLINE>
	 Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres.
	 <BLANKLINE>

Checking for ending in non-special char:
         >>> text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres""")
         Lorem ipsum dolor sit amet, consectetur adipiscing elit.
         <BLANKLINE>
         Quonam modo?
         <BLANKLINE>
         Utrum igitur tibi litteram videor an totas paginas commovere?
         <BLANKLINE>
         Non autem hoc:
         <BLANKLINE>
         igitur ne illud quidem.
         <BLANKLINE>
         Fortasse id optimum, sed ubi illud:
         <BLANKLINE>
         Plus semper voluptatis?
         <BLANKLINE>
         Teneo, inquit, finem illi videri nihil dolere.
         <BLANKLINE>
         Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.
         <BLANKLINE>
         Si id dicis, vicimus.
         <BLANKLINE>
         Inde sermone vario sex illa a Dipylo stadia confecimus.
         <BLANKLINE>
         Sin aliud quid voles, postea.
         <BLANKLINE>
         Quae animi affectio suum cuique tribuens atque hanc, quam dico.
         <BLANKLINE>
         Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres

Checking for multiple spaces:
	 >>> text_indentation("   Hello.  How are you?   ")
	 Hello.
	 <BLANKLINE>
	 How are you?
	 <BLANKLINE>

Checking for standalone special chars:
	 >>> text_indentation(" . ? : ")
	 .
	 <BLANKLINE>
	 ?
	 <BLANKLINE>
	 :
	 <BLANKLINE>

Checking for one word:
	 >>> text_indentation("Hello")
	 Hello

Checking for newline at beginning:
	 >>> text_indentation(" \n Hello. Whatcha up to?")
	 <BLANKLINE>
	  Hello.
	 <BLANKLINE>
	 Whatcha up to?
	 <BLANKLINE>
 
Checking for newline in middle:
	 >>> text_indentation("Hello \n . How are you?")
	 Hello 
	  .
	 <BLANKLINE>
	 How are you?
	 <BLANKLINE>

Checking for newline at end:
	 >>> text_indentation("Hello, how are you?\n")
	 Hello, how are you?
	 <BLANKLINE>
	 <BLANKLINE>

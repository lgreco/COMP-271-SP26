# How to Prepare for COMP 271 / COMP 400B

Coming into this course requires familiarity with the following **core programming skills:**

- **Arrays** (lists, in Python)  
  [Practice on LeetCode](https://leetcode.com/problem-list/v1e7rvrd/) during the winter break, email Leo for assistance.
- **Loops**  
  [`for`](https://docs.python.org/3/reference/compound_stmts.html#for),  
  [`while`](https://docs.python.org/3/reference/compound_stmts.html#while)
- **Conditionals**  
  [`if`](https://docs.python.org/3/reference/compound_stmts.html#if)
- **Strings**  
  [Practice on LeetCode](https://leetcode.com/problem-list/v1ei9bm1/)  during the winter break, email Leo for assistance.

You should also be comfortable working in a **programming environment**. If you have not yet committed to one, I recommend  
[Visual Studio Code](https://code.visualstudio.com/).

VS Code can be run:
- **Natively** on your own computer, or
- **Virtually** via **GitHub Codespaces**, which provides a cloud-based development environment.

GitHub is a central platform in the broader computing community, and creating a free account is strongly recommended. If you sign up using your `@luc.edu` email address, your account will automatically be upgraded to a higher tier at no cost to you. We'll review GitHub and Codespaces during our first week of classes.

There are two **important resources** that you should bookmark and visit frequently:

- [Python Language Reference](https://docs.python.org/3/reference/index.html), and
- [Python Standard Library](https://docs.python.org/3/library/index.html)

Knowing your way around these two resources is one of the best things you can learn about the Python programming language.

Finally, programming in general—and data structures in particular—requires a reasonable level of comfort with **algebra and calculus**. Mathematics is the *science* in *computer science*. You should review material from **COMP 163**, especially basic notation and symbolic reasoning, including:

- **number sets**  
  $\mathbb N$, $\mathbb R$, and subset notation, for example $\mathbb R_{<0}$
- **function declarations**  
  $f:\mathbb N\rightarrow \mathbb R$
- **quantifiers**  
  $\exists$, $\forall$
- **set membership**  
  $c\in\mathbb R_{>0}$
- **simple set operations and relations**  
  $\cup$, $\cap$, $\times$, $\subset$, $\supset$
- **important functions**  
  $\log_2n$, $e^n$, $n!$, $\binom{n}{k}$

With a bit of effort, you should be able to read, decode, and understand expressions such as the following:

$$
\begin{aligned}
&\text{Let } f,g : \mathbb{N} \to \mathbb{R}. \\
&g(n) \in \mathcal{O}(f(n))
\;\Longleftrightarrow\;
\exists\, c \in \mathbb{R}_{>0},\ \exists\, n_0 \in \mathbb{N}
\text{ such that} \\
&\forall\, n \in \mathbb{N},\ n \ge n_0,
g(n) \le c\,f(n).
\end{aligned}
$$

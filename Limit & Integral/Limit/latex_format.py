from sympy import oo
import latex

arr = [
    "\\lim_{x\\rightarrow0}{\\frac{x\\sin{5}x}{\\tan^2{2x}}}",
    "\\lim_{x\\rightarrow0}{\\frac{12x-4x^2}{\\sin{4}x}}",
    "\\lim_{x\\rightarrow0}{\\frac{\\cos{7}x-\\cos{3}x}{\\cos{4}x-1}}",
    "\\lim_{x\\rightarrow\\frac{\\pi}{12}}{\\frac{1-\\sin{6}x}{\\cos^2{6x}}}",
    "\\lim_{x\\rightarrow\\frac{\\pi}{4}}{\\frac{3\\cos^2{x}-\\sin^2{x}-\\sin{2}x}{\\cos^2{x}+\\sin{x}\\cos{x}-2\\sin^2{x}}}",
    "\\lim_{x\\rightarrow\\infty}{\\frac{\\left(2+3x\\right)\\left(1-x^2\\right)}{\\left(x+5\\right)\\left(x^2+3\\right)}}",
    "\\lim_{x\\rightarrow\\infty}{\\frac{\\tan{\\left(\\frac{3}{x}\\right)}+\\sin{\\left(\\frac{7}{x}\\right)}}{\\sin{\\left(\\frac{8}{x}\\right)}-\\tan{\\left(\\frac{3}{x}\\right)}}}",
    "\\lim_{x\\rightarrow\\infty}{\\sqrt{9x^2-12x+4}}-3x-1",
    "\\lim_{x\\rightarrow\\infty}{\\frac{\\left(ax-3\\right)^5}{8x^5+5x^3+2x-1}=4}",
    "\\lim_{x\\rightarrow3}{\\frac{6\\left(x^2-9\\right)tan\\left(x^2-6x+9\\right)}{\\left(3x-x^2\\right)\\sin^2{\\left(2x-6\\right)}}}"
]

close_to = [
    0, 0, 0, 15, 45,
    oo, oo, oo, oo, 3
]

'''
 For Online latex viewer
arr = [
\\1.\lim_{x\rightarrow0}{\frac{x\sin{5}x}{\tan^2{2x}}}=
\\\\2.\lim_{x\rightarrow0}{\frac{12x-4x^2}{\sin{4}x}}=
\\\\3.\lim_{x\rightarrow0}{\frac{\cos{7}x-\cos{3}x}{\cos{4}x-1}}=
\\\\4.\lim_{x\rightarrow\frac{\pi}{12}}{\frac{1-\sin{6}x}{\cos^2{6x}}}=
\\\\5.\lim_{x\rightarrow\frac{\pi}{4}}{\frac{3\cos^2{x}-\sin^2{x}-\sin{2}x}{\cos^2{x}+\sin{x}\cos{x}-2\sin^2{x}}}=
\\\\6.\lim_{x\rightarrow\infty}{\frac{\left(2+3x\right)\left(1-x^2\right)}{\left(x+5\right)\left(x^2+3\right)}}=
\\\\7.\lim_{x\rightarrow\infty}{\frac{\tan{\left(\frac{3}{x}\right)}+\sin{\left(\frac{7}{x}\right)}}{\sin{\left(\frac{8}{x}\right)}-\tan{\left(\frac{3}{x}\right)}}}=
\\\\8.\lim_{x\rightarrow\infty}{\sqrt{9x^2-12x+4}}-3x-1=
\\\\9.\lim_{x\rightarrow\infty}{\frac{\left(ax-3\right)^5}{8x^5+5x^3+2x-1}=4}
\\\\10.\lim_{x\rightarrow3}{\frac{6\left(x^2-9\right)tan\left(x^2-6x+9\right)}{\left(3x-x^2\right)\sin^2{\left(2x-6\right)}}=}
]
'''
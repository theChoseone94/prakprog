#ifndef HAVE_KOMPLEX_H
#define HAVE_KOMPLEX_H

struct komplex {double re; double im;};
typedef struct komplex komplex;

void	komplex_print	(char* s, komplex z); /* this prints s and then complex number z */
void	komplex_set	(komplex* z, double x, double y); /* sets z = x + i*y */
komplex	komplex_new	(double x, double y); /* returns x + i *y */
komplex	komplex_add	(komplex a, komplex b); /* returns a+b */
komplex	komplex_sub	(komplex a, komplex b); /* returns  a-b */


#endif

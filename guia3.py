
# coding: utf-8

# In[2]:

get_ipython().magic(u'pylab inline')
from IPython.html.widgets import interact


# # Ejercicio 4

# In[4]:

def amp(n, L):
    return 2*L*sin(n * pi / 2) / ((n**2) * pi**2)
def fourier(x, n):
    y = zeros_like(x)
    for i in xrange(1, n+1):
        y += armonico(x, i)
    return y
def armonico(x, n):
    L = x[-1]
    km = pi * n / L
    y = amp(n, L) * sin(km* x)
    return y


# In[ ]:

L = 1
x = linspace(0, L, 100)
figure(1)
title('Fundamental')
plot(x, armonico(x, 1), linewidth=2);
show()

for n in range(3, 10, 2):
    figure(n)
    title(str(n) + ' armonicos')
    plot(x, fourier(x, n - 2), linewidth=2, label='suma hasta ' + str(n-2));
    plot(x, armonico(x, n), linewidth=2, label='armonico ' + str(n))
    plot(x, fourier(x, n), linewidth=2, label='suma hasta ' + str(n))
    legend()#
    show()


# In[8]:

@interact(armonicos=(1, 40, 2))
def f(armonicos=1):
    L = 1
    x = linspace(0, L, 100)
    ylim([0, 0.25])
    plot(x, fourier(x, armonicos))


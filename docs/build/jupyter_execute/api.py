#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyCatSim as cats
nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')


# In[2]:


import pyCatSim as cats
nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')
nutmeg.make_noise()


# In[3]:


import pyCatSim as cats
nutmeg = cats.Cat(name='Nutmeg', age = 3, color = 'tortoiseshell')
nutmeg.play()


# In[4]:


from pyCatSim import Cat, Owner

cat1 = Cat(name="Whiskers")
cat2 = Cat(name="Boots", color="tabby")

# Single cat
owner1 = Owner(name="Sasha", cats_owned=cat1)

# Multiple cats
owner2 = Owner(name="Liam", cats_owned=[cat1, cat2])

print(owner1.name)
print([cat.name for cat in owner2.cats_owned])


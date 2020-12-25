c = """<div class="animal">
    <p class="name">
    <a title="Tiger"></a>
    </p>
    <p class="content">
    Two tigers two tigers run fast
    </p>
</div>
​
<div class="animal">
    <p class="name">
    <a title="Rabbit"></a>
    </p>
​
    <p class="content">
    Small white rabbit white and white
    </p>
</div>
"""
import re
pattern = re.compile('<a title=(.*?)></a>',re.S)
r = pattern.findall(c)
print(r)

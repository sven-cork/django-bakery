from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Recipies(models.Model):

    bake_category = [
        ('ci_bu', 'Cinnamon Bun'),
        ('da_pa', 'Danish Pastry'),
        ('ce_ca', 'Cheese Cake'),
        ('ch_ca', 'Chocolate Cake'),
        ('cr_ca', 'Cream Cake'),
        ('st_ca', 'Strawberry Cake'),
        ('ea_me', 'Eaton Mess'),
        ('ap_pi', 'Apple Pie'),
        ('co_ki', 'Cookies'),
        ('ea_me', 'Eaton Mess'),
        ('br_ee', 'Brulee'),
        ('ic_cr', 'Ice Cream'),
        ('br_ie', 'Brownie'),
        ('pa_es', 'Pancakes'),
        ('mu_ns', 'Muffins'),
        ('ti_su', 'Tiramisu'),
        ('tr_le', 'Trifle'),
    ]

    bake_category_cover = {
        'ci_bu': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876511/cinnamon_bun_pid0xd.jpg',
        'da_pa': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876619/danish_pastry_nuaq2q.jpg',
        'ce_ca': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876440/cheese_cake_udetjm.jpg',
        'ch_ca': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876481/chocolate_cake_wlj43x.jpg',
        'be_ca': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687874601/berry_cake_k0sg6d.jpg',
        'st_ca': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876941/strawberry_cake_x78lof.jpg',
        'ap_pi': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687802420/apple_pie_puxvsa.jpg',
        'co_ki': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876582/cookies_uedtzr.jpg',
        'ea_me': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876648/eaton_mess_fwcjav.jpg',
        'br_ee': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876941/brulee_rt3ef1.jpg',
        'ic_cr': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876691/ice_cream_zdq3eu.jpg',
        'br_ie': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876315/brownie_ek73q2.jpg',
        'pa_es': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876721/pancakes_frv4i4.jpg',
        'mu_ns': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876721/muffins_wobxne.jpg',
        'ti_su': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876768/tiramisu_npcwme.jpg',
        'tr_le': 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1687876768/trifle_eenoqq.jpg',
    }

    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name="recipie_posts")
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='recipie_likes', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()
    
    def number_of_comments(self):
        return self.comments.count()
    
    def get_absolute_url(self):
        return reverse("recipie_detail",  kwargs={"slug": self.slug})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipie = models.ForeignKey(Recipies, on_delete=models.CASCADE,
                                related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.name}"

    

    



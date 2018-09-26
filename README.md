# redis-routes


Install the python dependencies using pip 

```bash
$ pip install -r requeriments.txt
```


Configure poject by coping .env file 


```bash
$ cp .template.env .env
```

Add modify the Redis credentials, host and port 
variables

## Base Map

```bash
$ sudo apt-get install libgeos-dev
$ pip install https://github.com/matplotlib/basemap/archive/master.zip
``` 

## Bloom filters

     

What is a Bloom Filter?

A Bloom filter is a probabilistic data structure which provides an efficient way to verify that an entry is certainly not in a set. This makes it especially ideal when trying to search for items on expensive-to-access resources (such as over a network or disk): If I have a large on-disk database and I want to know if the key foo exists in it, I can query the Bloom filter first, which will tell me with a certainty whether it potentially exists (and then the disk lookup can continue) or whether it does not exist, and in this case I can forego the expensive disk lookup and simply send a negative reply up the stack.

While it’s possible to use other data structures (such as a hash table) to perform this, Bloom filters are also especially useful in that they occupy very little space per element, typically counted in the number of bits (not bytes!). There will exist a percentage of false positives (which is controllable), but for an initial test of whether a key exists in a set, they provide excellent speed and most importantly excellent space efficiency.

Bloom filters are used in a wide variety of applications such as ad serving – making sure a user doesn’t see an ad too often; likewise in content recommendation systems – ensuring recommendations don’t appear too often, in databases – quickly checking if an entry exists in a table before accessing it on disk, and so on.
How Bloom filters work


Getting the module and using it is very straightforward:
Downloading and building

You should first download and compile the module:
```bash
 $ git clone git://github.com/RedisLabsModules/rebloom
 $ cd rebloom
 $ make
```
 

You should now have a rebloom.so in the rebloom directory.
Loading Rebloom into Redis

Once you’ve built the filter module you, point your redis.conf or the redis command line to the module using loadmodule or –loadmodule respectively:

redis.conf:

loadmodule /path/to/rebloom.so

 

Command-line
```bash
    $ redis-server --loadmodule /path/to/rebloom.so

```

Trying It Out

You can play with it a bit using redis-cli:
```redis
    127.0.0.1:6379> BF.ADD bloom mark
 1) (integer) 1
 127.0.0.1:6379> BF.ADD bloom redis
 1) (integer) 1
 127.0.0.1:6379> BF.EXISTS bloom mark
 (integer) 1
 127.0.0.1:6379> BF.EXISTS bloom redis
 (integer) 1
 127.0.0.1:6379> BF.EXISTS bloom nonexist
 (integer) 0
 127.0.0.1:6379> BF.EXISTS bloom que?
 (integer) 0
 127.0.0.1:6379>
 127.0.0.1:6379> BF.MADD bloom elem1 elem2 elem3
 1) (integer) 1
 2) (integer) 1
 3) (integer) 1
 127.0.0.1:6379> BF.MEXISTS bloom elem1 elem2 elem3
 1) (integer) 1
 2) (integer) 1
 3) (integer) 1 
```
 
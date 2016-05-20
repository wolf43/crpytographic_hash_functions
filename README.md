# crpytographic_hash_functions
###Python file
The python file in this repo shows examples of computing hash of a string, contents of a file and contents of a web page. Rest of this doc is theoretical info about hash functions.

###Definition
Cryptographic hash functions are functions that take in a message as input and returns n bit output known as the digest. These functions are required to have the following properties :
* Preimage resistance : Given a digest h(m) for a message m, it is computationally infeasible to recover m. 
* Second preimage resistance : Given a message m1, it is computationally infeasible to find another message, m2 != m1, such that h(m1) == h(m2) 
* Collision resistance : It is computationally infeasible to find two distinct messages, m1 and m2, such that h(m1) == h(m2)

###Generic attacks
The generic attacks that apply to all hash functions are listed below. These attacks apply to all hash functions and should viewed as the upper bound to which a hash function is secure. 
* Preimage attacks : The generic preimage attack for a cryptographic hash function that produce n bit digest is brute force and requires 2^n hash evaluations, e.g. for a hash function that produces 160 bit digest, the generic preimage attack would take 2^160 hash evaluation. 
* Second preimage attack : The generic second preimage attack for an ideal cryptographic hash function also requires 2^n hash evaluations. 
* Collision resistance : The generic collision attack is the birthday attack and takes 2^(n/2) hash evaluations to achieve. 

###Broken hash function
Any hash function that doesn't provide the security guarantees that are listed in generic attacks is said to be "broken" from a cryptanalysis standpoint. Hash functions are used for a lot of different applications and it might still be okay to use a "broken" hash function depending on the application. On the flip side, attacks may exist against a particular application of hash functions and even "safe" hash functions(used directly) might not be secure to use. If this sounds confusing, it is. The various applications are listed in the applications section of this page and the correct hash functions to use/or not use for each application is mentioned.  
Another point that isn't always clear is that collisions always exist(in theory) for all commonly used hash functions. For example, in case of SHA 256 - any input of size up to 2^64 bits is mapped to an output of 256 bits, as the output space is much smaller than the input space, collisions are inevitable; but finding them using current day technology is computationally infeasible.

###Commonly used hash functions
####MD5 
MD5 produces an output digest of 128 bits. It uses a Merkel-Damgard construction and was first published by Ron Rivest(The R in RSA) in 1992. The best known collision attack against MD5 requires 2^18 hash computations and the preimage attack requires 2^123 hash computations, what that translates into english is - the collision resistance property of MD5 is badly broken(2^64 in theory to 2^18 in practice) and it shouldn't be used where that property is necessary. If you are the problem solving type, here is a MD5 hash you can play with and if you can break it, please email me and i'll mail you a very special gift :) : 5beab12ebff71920ddc6308526a8e514  
The biggest problem with MD5 hash function these days is perception. MD5 is broken from a collision resistance standpoint(if someone really wants to get two inputs to have the same MD5 hash, they can do it without too much headache). Cryptography is complicated and sometimes to drive home a point people say things like "MD5 is completely broken" without bothering people with the detailed cryptanalysis. So every time you use MD5 for anything, people will respond with "MD5 is wrong/broken" and you have to have long complicated conversations to explain why it is okay to use it in a particular scenario. From a PR(and not having to explain the same thing to everyone) standpoint, it is best to not use MD5 functions if possible. 
####SHA1
SHA1 produces an output digest of 160 bits. It also uses a Merkel-Damgard construction and was designed by the NSA and published in 1995. The best known collision attack against SHA1 is 2^51 hash evaluations, but this attack so far is only theoretical. However, it is advised that SHA1 functions not be used for future applications where collision resistance is required. Browsers started to issue SSL certificate errors for certificates signed with SHA1 digest starting 2016, so please plan to move to certificates that use SHA2 digest for the digital signature. Here is a SHA1 hash of the same message as MD5 : 00a1e709ad00b010081d3bbb626f806cd1564de8
####SHA2
SHA2 describes a family of functions that produce digests of sizes 224 bits, 256 bits, 384 bits and 512 bits. There are no real attacks against SHA2 family so far and are perfectly fine to use for most applications of hash functions(care must be taken for password storage, details in "applications" section below). Here is a digest from a SHA 512 (512 bits of output) : 6ab5c951baa963f98ef273b2c40b6b42f96ca40c1638b7153811aebe88fb9cf3bd3cafadd90ad71f93a0540b2b6064b6d50965660ac2960cc10e7b4004d6d871. Breaking this is extremely hard, but here's a hint https://xkcd.com/538/
####SHA3
In 2012 Keccak family of sponge functions were chosen by NIST as the SHA3 standard. The motivation was to choose a different construction after the advances in attacks against hash functions that use Merkel Damgard construction(MD5, SHA1 and SHA2 use that construction). There isn't a lot of support for SHA3 in programming languages yet, but it will slowly get added as it is a new standard. Here is a great table comparing different hash functions http://en.wikipedia.org/wiki/Template:Comparison_of_SHA_functions

###Applications
Hash functions are used in a lot of applications of cryptography and Bruce Schneier(who is a very well known cryptographer) called them the workhorses of modern cryptography. Some libraries provide functions that abstract the use of hash functions(and expose only the useful application) and some libraries might not and you would have to use the hash function along with the other primitive used for the construction. For example, you might have a library that gives you a function to generate a digital signature directly, but another library may require you to compute the hash and then apply the public key encryption on this digest to. The practical advice here is :
* Try to use the high level implementation of applications if available
* Do a quick search to see if there are any known issues with the function/version of the function you are about to use

####Digital Signatures
For use in digital signatures, the hash functions should have high collision resistance, therefore, MD5 should not be used(MD5 hash collision was used in flame malware to get a "forged" Microsoft certificate). You should also start a migration plan if you are using SHA1. For new applications, use SHA 256 when using for digital signatures. 
####MAC
For use in MAC, strong collision resistance is not important. So if you have an implementation of HMAC-MD5, you are probably fine. But for newer implementations use SHA2 family. 
####Password storage
Most hash functions mentioned here are fast, which is a problem because the sample space of passwords selected by most humans is tiny. Slow hash functions like bcrypt are best suited for this.
####Unique identifiers
This is where things get more interesting and you have to ask the questions - does the attacker control the input for the hash function and what happens if there is a collision?
If the attacker doesn't control the input to the hash function, any collision will be accidental. The probability of an accidental collision in a hash function is summed up by the birthday attack. For example, in case of SHA1 - output digest is 160 bits, you will find an accidental collision after 2^80 inputs(http://en.wikipedia.org/wiki/Yobibyte) with a 50% probability. Git uses SHA1 hash for its commit ID. Even for MD5, the change of an accidental collision is 50% after 2^64 samples. 
If the attacker does control the input, the collision resistance property becomes important and you should use one of the SHA2 family hash functions. The other important question to ask yourself is - what will happen if there is a collision? how will it impact your system?
####Cryptographically secure pseudo-random number generation
Hash functions are used to build some of these but you should not use hash functions directly to build a CSPRNG, this is one of the hardest things to get right. Please use the CSPRNG provided by the crpyto library you are using. 
####Integrity of software packages
It is a common practice to advertise the hash output of a software package in a public place, so that the users can validate the package before installing it. SHA-2 functions are best suited for it these days. There are other attacks against the page that you are advertising it on, i.e. an attacker can change the package and change the advertised hash on the page. For this, use a site only you control and use HTTPS. 
####Proof of work system
This is a very interesting application. The goal is to incur some cost to perform a certain action, the best example is spam - for every email sent, if we would make the senders machine do some work(computation), we would be able to deter spammers. Hashcash is a popular library that uses hash collision for this computation work. It will basically make the sender compute a partial second preimage for a value that varies and cant be stored in a precomputed table. Here are more details http://hashcash.org/faq/
####Others
Hash functions are also used in other areas such as KDF, hashsets, HOTP/TOTP(they use HMAC) and zero knowledge proof. It is a very powerful tool and hopefully after reading this, you will be more confident when using this tool in your applications.    
###Further recommended reading  
https://www.schneier.com/blog/archives/2012/10/when_will_we_se.html  
https://www.schneier.com/blog/archives/2005/02/sha1_broken.html  
http://people.csail.mit.edu/yiqun/SHA1AttackProceedingVersion.pdf (this was the paper that "broke" SHA1)  
http://en.wikipedia.org/wiki/Birthday_attack  
http://keccak.noekeon.org/  
http://www.hashhunters.net/  
http://www.hashcash.org/  
http://en.wikipedia.org/wiki/Pigeonhole_principle

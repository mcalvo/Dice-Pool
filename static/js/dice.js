;(function(root){
    // From http://baagoe.com/en/RandomMusings/javascript/
    // Johannes Baagøe <baagoe@baagoe.com>, 2010
    function Mash() {
        var  n = 0xefc8249d
            ,mash;

        mash = function(data) {
            data = data.toString();
            for (var i = 0; i < data.length; i++) {
                n += data.charCodeAt(i);
                var h = 0.02519603282416938 * n;
                n = h >>> 0;
                h -= n;
                h *= n;
                n = h >>> 0;
                h -= n;
                n += h * 0x100000000; // 2^32
            }
            return (n >>> 0) * 2.3283064365386963e-10; // 2^-32
        };

        mash.version = 'Mash 0.9';
        return mash;
    }

    // modified, from http://baagoe.com/en/RandomMusings/javascript/
    root.Alea = function Alea(){
        // Johannes Baagøe <baagoe@baagoe.com>, 2010
        var  args = [].slice.call(arguments)
            ,s0 = 0
            ,s1 = 0
            ,s2 = 0
            ,c = 1

            ,mash
            ,i
            ,random;

        if (args.length == 0) {
            args = [+new Date];
        }

        mash = Mash();
        s0 = mash(' ');
        s1 = mash(' ');
        s2 = mash(' ');

        for (i = 0; i < args.length; i++) {
            s0 -= mash(args[i]);
            if (s0 < 0) {
                s0 += 1;
            }
            s1 -= mash(args[i]);
            if (s1 < 0) {
                s1 += 1;
            }
            s2 -= mash(args[i]);
            if (s2 < 0) {
                s2 += 1;
            }
        }

        mash = null;

        random = function() {
            var t = 2091639 * s0 + c * 2.3283064365386963e-10; // 2^-32
            s0 = s1;
            s1 = s2;
            return s2 = t - (c = t | 0);
        };

        random.uint32 = function() {
            return random() * 0x100000000; // 2^32
        };

        random.fract53 = function() {
            return random() + 
                (random() * 0x200000 | 0) * 1.1102230246251565e-16; // 2^-53
        };

        random.version = 'Alea 0.9';
        random.args = args;
        return random;
    }

    // call a constructor with variable arguments
    // http://stackoverflow.com/questions/1606797/use-of-apply-with-new-operator-is-this-possible/1608546#1608546
    function construct(constructor, args) {
        function F() {
            return constructor.apply(this, args);
        }
        F.prototype = constructor.prototype;
        return new F();
    }

    root.Dice = function(seed){
        this.gen = construct(Alea, arguments);
    }

    root.Dice.prototype = (function make(){
        var types =  {}
                    ,i

        for(i = 2; i <= 100; i++){
            types['d' + i] = (function(sides){
                return function(count, separate){
                    count = count || 1;

                    var rolls = []
                        ,total = 0
                        ,i = 0
                        ,a;

                    for(;i < count; i++){
                        a = ((this.gen()*sides)|0) + 1;
                        total += a;
                        rolls.push(a);
                    }

                    return separate === true
                        ? rolls
                        : total;
                }
            })(i)
        }

        return types;
    })();

})(typeof module === 'undefined'
    ? window
    : exports);

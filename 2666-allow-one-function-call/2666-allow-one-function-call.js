/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let is_called = false ;
    return function(...args){
        if(!is_called){
            is_called = true 
            return fn(...args)
         
        }
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */

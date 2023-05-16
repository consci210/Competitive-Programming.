/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    const start = Date.now()
	return async function(...args) {
        result = Promise.race([fn(...args) , new Promise ( (success,reject)=>
          setTimeout( () =>reject("Time Limit Exceeded" ) ,t) )
         ])
        const end = Date.now()
        if ((end-start) > t){
            Throw("Time Limit Exceeded")
        }
        return result
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
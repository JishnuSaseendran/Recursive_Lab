var codes = {};
var freequency = function(str){

        var freq = {}
        for( ch in str)
        {
                if(freq[str[ch]] == undefined){
                        freq[str[ch]] = 1;}
                else{
                        freq[str[ch]]++;}       
        }
        return(freq)
}


var sortFreq = function(freq){

        tuples = []
                for( key in freq){
                        tuples.push(Array(freq[key],key))}
        return tuples.sort()

}

var buildTree = function(tuples){

        while(tuples.length > 1)
        {
                var leastTwo = tuples.slice(0,2);
                var theRest = tuples.slice(2,tuples.length);
                var combFreq = leastTwo[0][0] + leastTwo[1][0];
                tuples = theRest;
                tuples.push(Array(combFreq, leastTwo));
                tuples.sort();
        }
        return tuples[0];
}

var trimTree = function(tree){

        var p = tree[1]
                if(typeof p == 'string'){
                        return p;}
                else
                        return Array(trimTree(p[0]), trimTree(p[1]))

}

var assignCodes = function(node, pat){

      if(typeof node == 'string'){
        codes[node] = pat;}
      else{
        assignCodes(node[0],pat+"0");
        assignCodes(node[1],pat+"1");
        }
      return codes;        
}


var encode = function(str){

    var output ='';
    
    for(ch in str){
        output = output + codes[str[ch]];
    }
    return output;
}

var decode = function(tree, code){
    var str = ''
    var p = tree;
    for(bit in code){
        if(code[bit] == '0'){
            p = p[0];
        }
        else{
            p = p[1];
        }
        if(typeof p == 'string'){
            str = str + p;
           p = tree;
        }
      }
    return str;
}
var name = 'jishnu saseendran';
var freq =freequency(name);
var sort =sortFreq(freq);                  
console.log('The frequency of letters are:', sort);
var tree =buildTree(sort);
var stripTree = trimTree(tree);
assignCodes(stripTree, '');
console.log('The code for letters are:', codes);
var code = encode(name);
console.log('The Encoded version is:', code);
var str = decode(stripTree,code);
console.log('The Decoded version is:', str);
if(name == str){
    console.log('Decoded data matches the original name');
}

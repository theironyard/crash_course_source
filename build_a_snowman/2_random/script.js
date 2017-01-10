$( function(){

    //returns 1 through max, integers
    var random = function( max ){
        return Math.floor( Math.random() * max + 1 );
    };

    //returns true or false (random)
    //think of as a coin flip
    var flip = function(){
        return Math.random() > 0.49999;
    };

    //select the element with a class of "face" and change it's id attribute
    //to the string "face" plus a random integer 1-3 e.g. "face2"
    $( ".face" ).attr( "id", "face" + random( 3 ) );

    //select the element with a class of "arm" and change it's id attribute
    //to the string "arm" plus a random integer 1-3 e.g. "face3"
    $( ".arm" ).attr( "id", "arm" + random( 3 ) );

    //if flip returns true, toggle the active class of the selected element
    if( flip() ){
        //if #dec1 had the class "active" remove it, otherwise add it
        $( "#dec1" ).toggleClass( "active" );
    }
    
    if( flip() ){
        $( "#dec2" ).toggleClass( "active" );
    }
    if( flip() ){
        $( "#dec3" ).toggleClass( "active" );
    }
} );
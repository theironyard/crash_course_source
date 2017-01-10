$( function(){

    var random = function( max ){
        return Math.floor( Math.random() * max + 1 );
    };

    var flip = function(){
        return Math.random() > 0.49999;
    };

    var buildSnowman = function(){

        $( ".face" ).attr( "id", "face" + random( 3 ) );
        $( ".arm" ).attr( "id", "arm" + random( 3 ) );

        if( flip() ){
            $( "#dec1" ).toggleClass( "active" );
        }
        if( flip() ){
            $( "#dec2" ).toggleClass( "active" );
        }
        if( flip() ){
            $( "#dec3" ).toggleClass( "active" );
        }
    };

    $( ".button" ).on( "click", function( e ){

        buildSnowman();
        e.preventDefault();
    } );
} );
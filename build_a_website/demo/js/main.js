$( function(){

    var $buttons = $( "button.btn" ),
        $img     = $( ".animation figure" ),
        type;

    $buttons.on( "click", function( e ){

        type = $( this ).data( "type" );

        $img.removeAttr( "class" );
        $img.addClass( type );
    } );
} );
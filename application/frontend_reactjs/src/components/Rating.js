import '../styles/anime.css';

export default function Rating({ score }) {
    const rating_star_1 = score > 1 ? "fa fa-star checked" : "fa fa-star un-checked"; 
    const rating_star_2 = score > 3 ? "fa fa-star checked" : "fa fa-star un-checked"; 
    const rating_star_3 = score > 5 ? "fa fa-star checked" : "fa fa-star un-checked"; 
    const rating_star_4 = score > 7 ? "fa fa-star checked" : "fa fa-star un-checked"; 
    const rating_star_5 = score > 9 ? "fa fa-star checked" : "fa fa-star un-checked"; 

    return (
        <div className="anime-rating">
            <p className="anime-more-info">Rating:</p>
            <span className={ rating_star_1 }></span>
            <span class={ rating_star_2 }></span>
            <span class={ rating_star_3 }></span>
            <span class={ rating_star_4 }></span>
            <span class={ rating_star_5 }></span>
        </div>
    );
}
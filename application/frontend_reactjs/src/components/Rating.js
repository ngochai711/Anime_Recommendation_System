import '../styles/anime.css';

export default function Rating({ score }) {
    return (
        <div className="anime-rating">
            <p className="anime-more-info">Rating:</p>
            <span className={ "fa fa-star checked" }></span>
            <span class={ "fa fa-star checked" }></span>
            <span class={ "fa fa-star checked" }></span>
            <span class={ "fa fa-star checked" }></span>
            <span class={ "fa fa-star un-checked" }></span>
        </div>
    );
}
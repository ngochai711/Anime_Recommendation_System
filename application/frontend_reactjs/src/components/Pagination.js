import React, { useState } from 'react';
import ReactPaginate from 'react-paginate';
import Anime from '../components/Anime'
import '../styles/pagination.css'

function Items({ currentItems }) {
    return (
        <div className="paginated-container">
            {currentItems &&
                currentItems.map((item) => (
                    <Anime poster={item} title="Sword Art Online"  margin={0.35} />
                ))}
        </div>
    );
}

export default function Pagination({ itemsPerPage, items }) {
    const [itemOffset, setItemOffset] = useState(0);

    const endOffset = itemOffset + itemsPerPage;
    const currentItems = items.slice(itemOffset, endOffset);
    const pageCount = Math.ceil(items.length / itemsPerPage);

    const handlePageClick = (event) => {
        const newOffset = (event.selected * itemsPerPage) % items.length;
        setItemOffset(newOffset);
    };

    return (
        <>
            <Items currentItems={currentItems} />
            <ReactPaginate
                className="pagination"
                breakLabel="..."
                nextLabel="next >"
                onPageChange={handlePageClick}
                pageRangeDisplayed={5}
                pageCount={pageCount}
                previousLabel="< prev"
                renderOnZeroPageCount={null}
            />
        </>
    );
}
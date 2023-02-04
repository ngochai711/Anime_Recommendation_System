import React, { useState } from 'react';
import ReactPaginate from 'react-paginate';
import Anime from '../components/Anime'
import '../styles/pagination.css'

function Items({ currentItems }) {
    return (
        <div className="paginated-container">
            {currentItems &&
                currentItems.map((item) => (
                    <Anime id={item['ID']} poster={item} title={item['Name']}  margin={0.35} />
                ))}
        </div>
    );
}

export default function Pagination({ itemsPerPage, items }) {
    const [itemOffset, setItemOffset] = useState(0);

    console.log(items);
    if (items === null) return;

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
                nextLabel=">>"
                onPageChange={handlePageClick}
                pageRangeDisplayed={5}
                pageCount={pageCount}
                previousLabel="<<"
                renderOnZeroPageCount={null}
            />
        </>
    );
}
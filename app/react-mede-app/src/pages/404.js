/*home.jsx*/
import React from "react";

const NotFoundPage = () => {
    return (
        <div>
            <ul>
                {["Alex", "John", "Jaz", "fedrik", "missali"].map((user, idx) => {
                    return <li key={idx}>{user}</li>;
                })}
            </ul>
        </div>
    );
};

export default NotFoundPage;
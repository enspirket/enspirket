import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import '../style/MenuItem.css'

function MenuItem({
    product_id, 
    product_img, 
    product_name_eng, 
    product_name_chinese, 
    product_price,
    promotion_price}){
        const handleClick = () => {
            console.log({product_id, 
                product_img, 
                product_name_eng, 
                product_name_chinese, 
                product_price,
                promotion_price})
        }

        return (
            <Card onClick={handleClick}>
                <Card.Img variant="top" src="holder.js/100px180" />
                <Card.Body>
                    <Card.Title>{product_name_eng}</Card.Title>
                    <Card.Text>${product_price}</Card.Text>
                </Card.Body>
            </Card>
        );
}
export default MenuItem
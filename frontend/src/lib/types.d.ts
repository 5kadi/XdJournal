
//user
type UserListData = {
    id: number,
    username: string,
    is_active: boolean,
    avatar: string
}

type UserData = {
    id: number,
    username: string,
    is_active: boolean,
    avatar: string
    last_login: string | null,
    email: string,
    join_date: string,
}

//article blocks
type ArticleBlock = {
    id: number,
    blockData: {
        type: string,
        content: string
    }
}

//articles
type ArticleListData = {
    id: number,
    user: UserListData,
    create_date: string,
    header: string,
    header_media: string,
    header_content: string,
    like_count: number,
    comment_count: number
}

type ArticleData =  {
    id: number,
    user: UserListData,
    create_date: string,
    update_date: string
    header: string,
    content: Array<ArticleBlock>
    is_published: boolean,
    like_count: number,
    comment_count: number,
    is_owner: boolean,
    is_liked: boolean
}


//comments
type CommentListData = {
    id: number,
    user: UserListData,
    create_date: string,
    update_date: string | null,
    content: string,
    like_count: number,
    is_owner: boolean,
    is_liked: boolean
}

type ArticleComments = {
    results: Array<CommentListData>
    next: string,
    prev: string
}

